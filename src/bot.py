from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler, MessageHandler, filters
from telegram.error import BadRequest
from first_aid.first_aid import FirstAid


class MyBot:
    def __init__(self, TOKEN):
        self.app = ApplicationBuilder().token(TOKEN).build()
        self.first_aid = FirstAid(self)
        self.user_message_ids = {}

        # Регистрация обработчиков
        self.app.add_handler(CommandHandler("start", self.start))
        self.app.add_handler(CommandHandler("info", self.start))
        self.app.add_handler(CallbackQueryHandler(self.main_menu_handler, pattern='^reminders$|^first_aid_menu$'))
        self.app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.delete_user_message))

    def run(self):
        print("Starting bot...")
        self.app.run_polling()

    async def delete_user_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Удаление пользовательских сообщений."""
        if update.message:
            try:
                await update.message.delete()
            except Exception as e:
                print(f"Ошибка удаления сообщения: {e}")

    async def delete_previous_messages(self, chat_id, context: ContextTypes.DEFAULT_TYPE):
        """Удаление всех сообщений пользователя."""
        if chat_id in self.user_message_ids:
            for message_id in self.user_message_ids[chat_id]:
                try:
                    await context.bot.delete_message(chat_id=chat_id, message_id=message_id)
                except Exception as e:
                    print(f"Ошибка удаления сообщения {message_id}: {e}")
            self.user_message_ids[chat_id] = []

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Команда /start."""
        chat_id = update.effective_chat.id
        await self.delete_previous_messages(chat_id, context)

        keyboard = [
            [InlineKeyboardButton("Напоминания", callback_data="reminders")],
            [InlineKeyboardButton("Первая помощь", callback_data='first_aid_menu')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        message = await context.bot.send_message(chat_id, "Выберите опцию:", reply_markup=reply_markup)
        self.user_message_ids.setdefault(chat_id, []).append(message.message_id)

    async def main_menu_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Обработчик главного меню."""
        query = update.callback_query
        chat_id = update.effective_chat.id
        await self.delete_previous_messages(chat_id, context)

        if query:
            await query.answer()
            if query.data == 'first_aid_menu':
                await self.first_aid.first_aid_menu(update, context)
            else:
                message = await context.bot.send_message(chat_id, "Извините, эта функция пока не доступна.")
                self.user_message_ids[chat_id].append(message.message_id)
                keyboard = [
                    [InlineKeyboardButton("Напоминания", callback_data="reminders")],
                    [InlineKeyboardButton("Первая помощь", callback_data='first_aid_menu')],
                ]
                reply_markup = InlineKeyboardMarkup(keyboard)
                message = await context.bot.send_message(chat_id, "Выберите опцию:", reply_markup=reply_markup)
                self.user_message_ids.setdefault(chat_id, []).append(message.message_id)
