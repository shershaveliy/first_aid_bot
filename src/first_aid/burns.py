from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler
import os


class Burns:
    def __init__(self, bot, first_aid):
        self.bot = bot
        self.first_aid_main = first_aid
        self.register_handlers()

    def register_handlers(self):
        self.bot.app.add_handler(CallbackQueryHandler(self.main_burns_aid_info, pattern='^burns$'))
        self.bot.app.add_handler(CallbackQueryHandler(self.thermal_burns, pattern='^thermal_burns$'))
        self.bot.app.add_handler(CallbackQueryHandler(self.chemical_burns, pattern='^chemical_burns$'))
        self.bot.app.add_handler(CallbackQueryHandler(self.sun_burns, pattern='^sun_burns$'))
        self.bot.app.add_handler(CallbackQueryHandler(self.electric_burns, pattern='^electric_burns$'))


    async def main_burns_aid_info(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        chat_id = update.effective_chat.id
        query = update.callback_query

        # Ответ на callback
        if query:
            await query.answer()
            
        await self.bot.delete_previous_messages(chat_id, context)

        main_text = r'C:\Users\jelena\Desktop\new_bot\med-bot\src\first_aid\first_aid_text\burns\main_burns.txt'

        try:
            with open(main_text, 'r', encoding='utf-8') as file:
                main_text = file.read()
        except FileNotFoundError:
            print(f"Файл {main_text} не найден")

        keyboard = [
            [InlineKeyboardButton("Термические ожоги", callback_data='thermal_burns')],
            [InlineKeyboardButton("Химические ожоги", callback_data='chemical_burns')],
            [InlineKeyboardButton("Солнечные ожоги", callback_data='sun_burns')],
            [InlineKeyboardButton("Электрические ожоги", callback_data='electric_burns')],
            [InlineKeyboardButton("Назад в меню первой помощи", callback_data='back_to_menu')],
            [InlineKeyboardButton("Назад в главное меню", callback_data='restart_bot')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        message = await context.bot.send_message(chat_id=chat_id, text=main_text, reply_markup=reply_markup, parse_mode='Markdown')
        self.bot.user_message_ids[chat_id].append(message.message_id)

    async def thermal_burns(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        chat_id = update.effective_chat.id
        query = update.callback_query

        # Ответ на callback
        if query:
            await query.answer()
            
        await self.bot.delete_previous_messages(chat_id, context)

        text_ = r'C:\Users\jelena\Desktop\new_bot\med-bot\src\first_aid\first_aid_text\burns\thermal_burns.txt'

        try:
            with open(text_, 'r', encoding='utf-8') as file:
                text = file.read()
        except FileNotFoundError:
            print(f"Файл {text} не найден")

        keyboard = [
            [InlineKeyboardButton("Назад в раздел ожогов", callback_data='burns')],
            [InlineKeyboardButton("Назад в меню первой помощи", callback_data='back_to_menu')],
            [InlineKeyboardButton("Назад в главное меню", callback_data='restart_bot')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        message = await context.bot.send_message(chat_id=chat_id, text=text, reply_markup=reply_markup, parse_mode='Markdown')
        self.bot.user_message_ids[chat_id].append(message.message_id)
        
    async def chemical_burns(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        chat_id = update.effective_chat.id
        query = update.callback_query

        # Ответ на callback
        if query:
            await query.answer()
            
        await self.bot.delete_previous_messages(chat_id, context)

        text_ = r'C:\Users\jelena\Desktop\new_bot\med-bot\src\first_aid\first_aid_text\burns\chemical_burns.txt'

        try:
            with open(text_, 'r', encoding='utf-8') as file:
                main_text = file.read()
        except FileNotFoundError:
            print(f"Файл {main_text} не найден")
        message = await context.bot.send_message(chat_id=chat_id, text=main_text, parse_mode='Markdown')
        self.bot.user_message_ids[chat_id].append(message.message_id)
        
        video_path = r'C:\Users\jelena\Desktop\new_bot\med-bot\src\first_aid\first_aid_photos\ozhogi.mp4'

        keyboard = [
            [InlineKeyboardButton("Назад в раздел ожогов", callback_data='burns')],
            [InlineKeyboardButton("Назад в меню первой помощи", callback_data='back_to_menu')],
            [InlineKeyboardButton("Назад в главное меню", callback_data='restart_bot')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        try:
            message = await context.bot.send_video(
                chat_id=chat_id,
                video=open(video_path, 'rb'),
                caption="Первая помощь при химических ожогах",
                supports_streaming=True,
                reply_markup=reply_markup,
                parse_mode='Markdown'
            )
        except Exception as e:
            print(f"Ошибка: {e}")
        self.bot.user_message_ids[chat_id].append(message.message_id)

    async def sun_burns(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        chat_id = update.effective_chat.id
        query = update.callback_query

        # Ответ на callback
        if query:
            await query.answer()
            
        await self.bot.delete_previous_messages(chat_id, context)

        text_ = r'C:\Users\jelena\Desktop\new_bot\med-bot\src\first_aid\first_aid_text\burns\sun_burns.txt'

        try:
            with open(text_, 'r', encoding='utf-8') as file:
                text = file.read()
        except FileNotFoundError:
            print(f"Файл {text} не найден")

        keyboard = [
            [InlineKeyboardButton("Назад в раздел ожогов", callback_data='burns')],
            [InlineKeyboardButton("Назад в меню первой помощи", callback_data='back_to_menu')],
            [InlineKeyboardButton("Назад в главное меню", callback_data='restart_bot')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        message = await context.bot.send_message(chat_id=chat_id, text=text, reply_markup=reply_markup, parse_mode='Markdown')
        self.bot.user_message_ids[chat_id].append(message.message_id)

    async def electric_burns(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        chat_id = update.effective_chat.id
        query = update.callback_query

        # Ответ на callback
        if query:
            await query.answer()
            
        await self.bot.delete_previous_messages(chat_id, context)

        text_ = r'C:\Users\jelena\Desktop\new_bot\med-bot\src\first_aid\first_aid_text\burns\electric_burns.txt'

        try:
            with open(text_, 'r', encoding='utf-8') as file:
                text = file.read()
        except FileNotFoundError:
            print(f"Файл {text} не найден")

        keyboard = [
            [InlineKeyboardButton("Термические ожоги", callback_data='thermal_burns')],
            [InlineKeyboardButton("Назад в раздел ожогов", callback_data='burns')],
            [InlineKeyboardButton("Назад в меню первой помощи", callback_data='back_to_menu')],
            [InlineKeyboardButton("Назад в главное меню", callback_data='restart_bot')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        message = await context.bot.send_message(chat_id=chat_id, text=text, reply_markup=reply_markup, parse_mode='Markdown')
        self.bot.user_message_ids[chat_id].append(message.message_id)