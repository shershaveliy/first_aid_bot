from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler, MessageHandler, filters
from telegram.error import BadRequest
from first_aid.first_aid import FirstAid


class MyBot:

    def __init__(self, TOKEN):
        self.app = ApplicationBuilder().token(TOKEN).build()
        self.first_aid = FirstAid(self)
        self.app.add_handler(CommandHandler("start", self.start))
        self.app.add_handler(CommandHandler("info", self.start))
        self.app.add_handler(CallbackQueryHandler(self.main_menu_handler, pattern='^reminders$|^first_aid_menu$'))
        self.app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.delete_user_message))
        self.user_message_ids = {}  # Словарь для хранения сообщений пользователей


    def run(self):
        print("Starting bot...")
        self.app.run_polling()

    async def delete_user_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Удаление пользовательских сообщений."""
        if update.message:
            try:
                await update.message.delete()
            except Exception as e:
                print(f"Не удалось удалить пользовательское сообщение: {e}")

    async def delete_previous_messages(self, chat_id, context: ContextTypes.DEFAULT_TYPE):
        """Удаление предыдущих сообщений для конкретного пользователя."""
        if chat_id in self.user_message_ids:
            for message_id in self.user_message_ids[chat_id]:
                try:
                    await context.bot.delete_message(chat_id=chat_id, message_id=message_id)
                except Exception as e:
                    print(f"Не удалось удалить сообщение {message_id}: {e}")
            self.user_message_ids[chat_id] = []  # Очищаем список сообщений для пользователя

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Обработка команды /start."""
        chat_id = update.effective_chat.id
        await self.delete_previous_messages(chat_id, context)

        # Удаляем пользовательское сообщение, если оно существует
        if update.message:
            await self.delete_user_message(update, context)

        # Отправляем главное меню
        keyboard = [
            [InlineKeyboardButton("Напоминания", callback_data="reminders")],
            [InlineKeyboardButton("Первая помощь", callback_data='first_aid_menu')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        try:
            message = await context.bot.send_message(chat_id=chat_id, text="Выберите опцию:", reply_markup=reply_markup)

            # Сохраняем ID сообщения для конкретного пользователя
            if chat_id not in self.user_message_ids:
                self.user_message_ids[chat_id] = []
            self.user_message_ids[chat_id].append(message.message_id)
        except Exception as e:
            print(f"Ошибка отправки сообщения в start: {e}")

    async def main_menu_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Обработка главного меню."""
        query = update.callback_query
        chat_id = update.effective_chat.id

        if not query:
            print("Ошибка: callback_query отсутствует.")
            return

        await self.delete_previous_messages(chat_id, context)

        try:
            await query.answer()
            print("Получено callback_data:", query.data)

            if query.data == 'first_aid_menu':
                await self.first_aid.first_aid_menu(update, context)
            else:
                # Проверяем, можно ли редактировать сообщение
                if query.message:
                    try:
                        message = await query.edit_message_text("Неизвестная команда.")
                        self.user_message_ids[chat_id].append(message.message_id)
                    except BadRequest as e:
                        if str(e) == "Message to edit not found":
                            message = await context.bot.send_message(
                                chat_id=chat_id,
                                text="Неизвестная команда."
                            )
                            self.user_message_ids[chat_id].append(message.message_id)
                        else:
                            raise
                else:
                    message = await context.bot.send_message(
                        chat_id=chat_id,
                        text="Неизвестная команда."
                    )
                    self.user_message_ids[chat_id].append(message.message_id)

        except Exception as e:
            print(f"Ошибка обработки main_menu_handler: {e}")
