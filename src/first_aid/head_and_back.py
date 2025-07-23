from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler
import os


class Head_and_back:
    def __init__(self, bot, first_aid):
        self.bot = bot
        self.first_aid_main = first_aid
        self.register_handlers()

    def register_handlers(self):
        self.bot.app.add_handler(CallbackQueryHandler(self.main_head_and_back_aid_info, pattern='^head_and_back$'))


    async def main_head_and_back_aid_info(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        chat_id = update.effective_chat.id
        query = update.callback_query

        # Ответ на callback
        if query:
            await query.answer()
            
        await self.bot.delete_previous_messages(chat_id, context)

        text_ = os.path.join('src', 'first_aid', 'first_aid_text', 'head_and_back', 'main_head_and_back.txt')

        try:
            with open(text_, 'r', encoding='utf-8') as file:
                main_text = file.read()
        except FileNotFoundError:
            print(f"Файл {main_text} не найден")
        message = await context.bot.send_message(chat_id=chat_id, text=main_text, parse_mode='Markdown')
        self.bot.user_message_ids[chat_id].append(message.message_id)
        

        video_path = os.path.join('src', 'first_aid', 'first_aid_photos', 'travmy-pozvonochnika.mp4')

        try:
            message = await context.bot.send_video(
                chat_id=chat_id,
                video=open(video_path, 'rb'),  # Открываем файл в бинарном режиме
                caption="Нажмите: [Травма позвоночника](https://mchs.gov.ru/deyatelnost/bezopasnost-grazhdan/travmy-pozvonochnika_4), чтобы получить информацию с сайта МЧС России.",  # Опциональная подпись
                supports_streaming=True,
                parse_mode='Markdown'
            )
        except Exception as e:
            print(f"Ошибка: {e}")
        self.bot.user_message_ids[chat_id].append(message.message_id)

        video_path = os.path.join('src', 'first_aid', 'first_aid_photos', 'travmy-golovy.mp4')

        keyboard = [
            [InlineKeyboardButton("Назад в меню первой помощи", callback_data='back_to_menu')],
            [InlineKeyboardButton("Назад в главное меню", callback_data='restart_bot')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        try:
            message = await context.bot.send_video(
                chat_id=chat_id,
                video=open(video_path, 'rb'),  # Открываем файл в бинарном режиме
                caption="Нажмите: [Травма головы](https://mchs.gov.ru/deyatelnost/bezopasnost-grazhdan/travmy-golovy_1), чтобы получить информацию с сайта МЧС России.",  # Опциональная подпись
                supports_streaming=True,
                reply_markup=reply_markup,
                parse_mode='Markdown'
            )
        except Exception as e:
            print(f"Ошибка: {e}")
        self.bot.user_message_ids[chat_id].append(message.message_id)