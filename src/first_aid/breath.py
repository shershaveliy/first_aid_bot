from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler
import os


class Breath:
    def __init__(self, bot, first_aid):
        self.bot = bot
        self.first_aid_main = first_aid
        self.register_handlers()

    def register_handlers(self):
        self.bot.app.add_handler(CallbackQueryHandler(self.main_breath_aid_info, pattern='^breath$'))


    async def main_breath_aid_info(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        chat_id = update.effective_chat.id
        query = update.callback_query

        # Ответ на callback
        if query:
            await query.answer()
            
        await self.bot.delete_previous_messages(chat_id, context)
        
        photo_path = os.path.join('src', 'first_aid', 'first_aid_photos', 'breath.jpg')
        message = await context.bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))
        self.bot.user_message_ids[chat_id].append(message.message_id)

        text_with_link_path = os.path.join('src', 'first_aid', 'first_aid_text', 'breath', 'main_breath.txt')

        try:
            with open(text_with_link_path, 'r', encoding='utf-8') as file:
                main_text = file.read()
        except FileNotFoundError:
            print(f"Файл {main_text} не найден")
        message = await context.bot.send_message(chat_id=chat_id, text=main_text, parse_mode='Markdown')
        self.bot.user_message_ids[chat_id].append(message.message_id)
        
        
        video_path = os.path.join('src', 'first_aid', 'first_aid_photos', 'chelovek-podavilsya-chto-delat.mp4')

        keyboard = [
            [InlineKeyboardButton("Реанимация (СЛР)", callback_data='aid_reanimation')],
            [InlineKeyboardButton("Назад в меню первой помощи", callback_data='back_to_menu')],
            [InlineKeyboardButton("Назад в главное меню", callback_data='restart_bot')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        try:
            message = await context.bot.send_video(
                chat_id=chat_id,
                video=open(video_path, 'rb'),
                caption="Нажмите: [здесь](https://29.mchs.gov.ru/deyatelnost/bezopasnost-grazhdan/neprohodimost-dyhatelnyh-putey), чтобы получить информацию с сайта МЧС России.",
                supports_streaming=True,
                reply_markup=reply_markup,
                parse_mode='Markdown'
            )
        except Exception as e:
            print(f"Ошибка: {e}")
        self.bot.user_message_ids[chat_id].append(message.message_id)