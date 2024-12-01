from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CallbackQueryHandler


class InjuryAid:
    def __init__(self, bot, first_aid):
        self.bot = bot
        self.first_aid_main = first_aid
        self.register_handlers()

    def register_handlers(self):
        self.bot.app.add_handler(CallbackQueryHandler(self.provide_injury_aid_info, pattern='^aid_injury$'))
        self.bot.app.add_handler(CallbackQueryHandler(self.Prellungent_aid_info, pattern='^Prellungent$'))
        self.bot.app.add_handler(CallbackQueryHandler(self.Verstauchung_aid_info, pattern='^Verstauchung$'))
        self.bot.app.add_handler(CallbackQueryHandler(self.Frakturen_aid_info, pattern='^Frakturen$'))
        self.bot.app.add_handler(CallbackQueryHandler(self.Luxationen_aid_info, pattern='^Luxationen$'))
        self.bot.app.add_handler(CallbackQueryHandler(self.rib_fracture_info, pattern='^rib_fracture$'))


    async def provide_injury_aid_info(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        chat_id = update.effective_chat.id
        query = update.callback_query

        if query:
            await query.answer()
            
        await self.bot.delete_previous_messages(chat_id, context)

        main_text = r'C:\Users\jelena\Desktop\new_bot\med-bot\src\first_aid\first_aid_text\injury\main_injury.txt'

        try:
            with open(main_text, 'r', encoding='utf-8') as file:
                main_text = file.read()
        except FileNotFoundError:
            print(f"Файл {main_text} не найден")
        message = await context.bot.send_message(chat_id=chat_id, text=main_text, parse_mode='Markdown')
        self.bot.user_message_ids[chat_id].append(message.message_id)
        
        video_path = r'C:\Users\jelena\Desktop\new_bot\med-bot\src\first_aid\first_aid_photos\travmy-konechnostey.mp4'

        keyboard = [
            [InlineKeyboardButton("Вывихи", callback_data='Luxationen')],
            [InlineKeyboardButton("Переломы", callback_data='Frakturen')],
            [InlineKeyboardButton("Ушибы (синяки)", callback_data='Prellungent')],
            [InlineKeyboardButton("Разрывы или растяжения связок, сухожилий.", callback_data='Verstauchung')],
            [InlineKeyboardButton("Раны с инородным телом", callback_data='foreign_body')],
            [InlineKeyboardButton("Назад в меню первой помощи", callback_data='back_to_menu')],
            [InlineKeyboardButton("Назад в главное меню", callback_data='restart_bot')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        try:
            message = await context.bot.send_video(
                chat_id=chat_id,
                video=open(video_path, 'rb'),
                caption="Травма конечностей",
                supports_streaming=True,
                reply_markup=reply_markup,
                parse_mode='Markdown'
            )
        except Exception as e:
            print(f"Ошибка: {e}")
        self.bot.user_message_ids[chat_id].append(message.message_id)

    async def Prellungent_aid_info(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        chat_id = update.effective_chat.id
        query = update.callback_query

        if query:
            await query.answer()
            
        await self.bot.delete_previous_messages(chat_id, context)

        photo_path = r'C:\Users\jelena\Desktop\new_bot\med-bot\src\first_aid\first_aid_photos\7278381c00c2c88e9180b07131e80552.jpg'
        message = await context.bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))
        self.bot.user_message_ids[chat_id].append(message.message_id)

        main_text = r'C:\Users\jelena\Desktop\new_bot\med-bot\src\first_aid\first_aid_text\injury\prellungent.txt'

        try:
            with open(main_text, 'r', encoding='utf-8') as file:
                main_text = file.read()
        except FileNotFoundError:
            print(f"Файл {main_text} не найден")
        keyboard = [
            [InlineKeyboardButton("Назад в раздел травмы", callback_data='aid_injury')],
            [InlineKeyboardButton("Назад в меню первой помощи", callback_data='back_to_menu')],
            [InlineKeyboardButton("Назад в главное меню", callback_data='restart_bot')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        message = await context.bot.send_message(chat_id=chat_id, text=main_text, reply_markup=reply_markup, parse_mode='Markdown'
        )
        self.bot.user_message_ids[chat_id].append(message.message_id)

    async def Verstauchung_aid_info(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        chat_id = update.effective_chat.id
        query = update.callback_query

        if query:
            await query.answer()
            
        await self.bot.delete_previous_messages(chat_id, context)

        photo_path = r'C:\Users\jelena\Desktop\new_bot\med-bot\src\first_aid\first_aid_photos\Verstauchung.jpg'
        message = await context.bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))
        self.bot.user_message_ids[chat_id].append(message.message_id)

        main_text = r'C:\Users\jelena\Desktop\new_bot\med-bot\src\first_aid\first_aid_text\injury\verstauchung.txt'

        try:
            with open(main_text, 'r', encoding='utf-8') as file:
                main_text = file.read()
        except FileNotFoundError:
            print(f"Файл {main_text} не найден")
        keyboard = [
            [InlineKeyboardButton("Назад в раздел травмы", callback_data='aid_injury')],
            [InlineKeyboardButton("Назад в меню первой помощи", callback_data='back_to_menu')],
            [InlineKeyboardButton("Назад в главное меню", callback_data='restart_bot')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        message = await context.bot.send_message(chat_id=chat_id, text=main_text, reply_markup=reply_markup, parse_mode='Markdown'
        )
        self.bot.user_message_ids[chat_id].append(message.message_id)

    async def Luxationen_aid_info(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        chat_id = update.effective_chat.id
        query = update.callback_query

        if query:
            await query.answer()
            
        await self.bot.delete_previous_messages(chat_id, context)

        photo_path = r'C:\Users\jelena\Desktop\new_bot\med-bot\src\first_aid\first_aid_photos\dislocation.jpg'
        message = await context.bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))
        self.bot.user_message_ids[chat_id].append(message.message_id)

        main_text = r'C:\Users\jelena\Desktop\new_bot\med-bot\src\first_aid\first_aid_text\injury\luxationen.txt'

        try:
            with open(main_text, 'r', encoding='utf-8') as file:
                main_text = file.read()
        except FileNotFoundError:
            print(f"Файл {main_text} не найден")
        keyboard = [
            [InlineKeyboardButton("Назад в раздел травмы", callback_data='aid_injury')],
            [InlineKeyboardButton("Назад в меню первой помощи", callback_data='back_to_menu')],
            [InlineKeyboardButton("Назад в главное меню", callback_data='restart_bot')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        message = await context.bot.send_message(chat_id=chat_id, text=main_text, reply_markup=reply_markup, parse_mode='Markdown'
        )
        self.bot.user_message_ids[chat_id].append(message.message_id)

    async def Frakturen_aid_info(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        chat_id = update.effective_chat.id
        query = update.callback_query

        if query:
            await query.answer()
            
        await self.bot.delete_previous_messages(chat_id, context)

        photo_path = r'C:\Users\jelena\Desktop\new_bot\med-bot\src\first_aid\first_aid_photos\Frakturen2.jpg'
        message = await context.bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))
        self.bot.user_message_ids[chat_id].append(message.message_id)

        main_text = r'C:\Users\jelena\Desktop\new_bot\med-bot\src\first_aid\first_aid_text\injury\Frakturen.txt'

        try:
            with open(main_text, 'r', encoding='utf-8') as file:
                main_text = file.read()
        except FileNotFoundError:
            print(f"Файл {main_text} не найден")
        keyboard = [
            [InlineKeyboardButton("Перелом рёбер", callback_data='rib_fracture')],
            [InlineKeyboardButton("Травма позвоночиника", callback_data='head_and_back')],
            [InlineKeyboardButton("Предотвращение кровотечения", callback_data='bleeding')],
            [InlineKeyboardButton("Назад в раздел травмы", callback_data='aid_injury')],
            [InlineKeyboardButton("Назад в меню первой помощи", callback_data='back_to_menu')],
            [InlineKeyboardButton("Назад в главное меню", callback_data='restart_bot')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        message = await context.bot.send_message(chat_id=chat_id, text=main_text, reply_markup=reply_markup, parse_mode='Markdown'
        )
        self.bot.user_message_ids[chat_id].append(message.message_id)

    async def rib_fracture_info(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        chat_id = update.effective_chat.id
        query = update.callback_query

        if query:
            await query.answer()
            
        await self.bot.delete_previous_messages(chat_id, context)

        photo_path = r'C:\Users\jelena\Desktop\new_bot\med-bot\src\first_aid\first_aid_photos\perelom-reber.jpg'
        message = await context.bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))
        self.bot.user_message_ids[chat_id].append(message.message_id)

        main_text = r'C:\Users\jelena\Desktop\new_bot\med-bot\src\first_aid\first_aid_text\injury\rib_fracturen.txt'

        try:
            with open(main_text, 'r', encoding='utf-8') as file:
                main_text = file.read()
        except FileNotFoundError:
            print(f"Файл {main_text} не найден")
        keyboard = [
            [InlineKeyboardButton("Рана грудной клетки", callback_data='rib_cage')],
            [InlineKeyboardButton("Назад в раздел травмы", callback_data='aid_injury')],
            [InlineKeyboardButton("Назад в меню первой помощи", callback_data='back_to_menu')],
            [InlineKeyboardButton("Назад в главное меню", callback_data='restart_bot')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        message = await context.bot.send_message(chat_id=chat_id, text=main_text, reply_markup=reply_markup, parse_mode='Markdown'
        )
        self.bot.user_message_ids[chat_id].append(message.message_id)
   