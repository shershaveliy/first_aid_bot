from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler
import os


class Bites:
    def __init__(self, bot, first_aid):
        self.bot = bot
        self.first_aid_main = first_aid
        self.register_handlers()

    def register_handlers(self):
        self.bot.app.add_handler(CallbackQueryHandler(self.main_bites_aid_info, pattern='^bites$'))


    async def main_bites_aid_info(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        chat_id = update.effective_chat.id
        query = update.callback_query

        # Ответ на callback
        if query:
            await query.answer()
            
        await self.bot.delete_previous_messages(chat_id, context)

        text_with_link_path = os.path.join('src', 'first_aid', 'first_aid_text', 'bites', 'bites.txt')

        try:
            with open(text_with_link_path, 'r', encoding='utf-8') as file:
                main_text = file.read()
        except FileNotFoundError:
            print(f"Файл {main_text} не найден")
        keyboard = [
            [InlineKeyboardButton("Назад в меню первой помощи", callback_data='back_to_menu')],
            [InlineKeyboardButton("Назад в главное меню", callback_data='restart_bot')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        message = await context.bot.send_message(chat_id=chat_id, text=main_text, reply_markup=reply_markup, parse_mode='Markdown')
        self.bot.user_message_ids[chat_id].append(message.message_id)
