from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CallbackQueryHandler
import os


class BleedingAid:
    def __init__(self, bot, first_aid):
        self.bot = bot
        self.first_aid_main = first_aid
        self.register_handlers()

    def register_handlers(self):
        self.bot.app.add_handler(CallbackQueryHandler(self.main_provide_bleeding_aid_info, pattern='^aid_bleeding$'))
        self.bot.app.add_handler(CallbackQueryHandler(self.abrasions_aid_info, pattern='^abrasions$'))
        self.bot.app.add_handler(CallbackQueryHandler(self.foreign_body_aid_info, pattern='^foreign_body$'))
        self.bot.app.add_handler(CallbackQueryHandler(self.rib_cage_aid_info, pattern='^rib_cage$'))
        self.bot.app.add_handler(CallbackQueryHandler(self.abdominal_injury_aid_info, pattern='^abdominal_injury$'))
        self.bot.app.add_handler(CallbackQueryHandler(self.bleeding_aid_info, pattern='^bleeding$'))
        self.bot.app.add_handler(CallbackQueryHandler(self.bleeding1_aid_info, pattern='^bleeding1$'))
        self.bot.app.add_handler(CallbackQueryHandler(self.bleeding2_aid_info, pattern='^bleeding2$'))
        self.bot.app.add_handler(CallbackQueryHandler(self.bleeding3_aid_info, pattern='^bleeding3$'))
        self.bot.app.add_handler(CallbackQueryHandler(self.eye_injuries_aid_info, pattern='^eye_injuries$'))


    async def main_provide_bleeding_aid_info(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        chat_id = update.effective_chat.id
        query = update.callback_query

        if query:
            await query.answer()
            
        await self.bot.delete_previous_messages(chat_id, context)

        main_text = os.path.join('src', 'first_aid', 'first_aid_text', 'bleeding', 'main_bleeding.txt')

        try:
            with open(main_text, 'r', encoding='utf-8') as file:
                main_text = file.read()
        except FileNotFoundError:
            print(f"Файл {main_text} не найден")

        keyboard = [
            [InlineKeyboardButton("Остановка кровотечения", callback_data='bleeding')],
            [InlineKeyboardButton("Ссадины/порезы", callback_data='abrasions')],
            [InlineKeyboardButton("Раны с инородным телом", callback_data='foreign_body')],
            [InlineKeyboardButton("Ранения глаз", callback_data='eye_injuries')],
            [InlineKeyboardButton("Ранение грудной клетки", callback_data='rib_cage')],
            [InlineKeyboardButton("Ранение брюшной полости", callback_data='abdominal_injury')],
            [InlineKeyboardButton("Действия при отрыве части тела", callback_data='bleeding2')],
            [InlineKeyboardButton("Назад в меню первой помощи", callback_data='back_to_menu')],
            [InlineKeyboardButton("Назад в главное меню", callback_data='restart_bot')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        message = await context.bot.send_message(chat_id=chat_id, text=main_text, reply_markup=reply_markup, parse_mode='Markdown'
        )
        self.bot.user_message_ids[chat_id].append(message.message_id)


    async def bleeding_aid_info(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        chat_id = update.effective_chat.id
        query = update.callback_query

        if query:
            await query.answer()
            
        await self.bot.delete_previous_messages(chat_id, context)

        photo_path = os.path.join('src', 'first_aid', 'first_aid_photos', 'jgyt.png')
        message = await context.bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))
        self.bot.user_message_ids[chat_id].append(message.message_id)

        main_text = os.path.join('src', 'first_aid', 'first_aid_text', 'bleeding', 'bleeding.txt')

        try:
            with open(main_text, 'r', encoding='utf-8') as file:
                main_text = file.read()
        except FileNotFoundError:
            print(f"Файл {main_text} не найден")
        message = await context.bot.send_message(chat_id=chat_id, text=main_text, parse_mode='Markdown')
        self.bot.user_message_ids[chat_id].append(message.message_id)

        video_path = os.path.join('src', 'first_aid', 'first_aid_photos', 'krovotecheniya.mp4')

        keyboard = [
            [InlineKeyboardButton("Первая помощь при внутреннем кровотечении", callback_data='bleeding1')],
            [InlineKeyboardButton("Первая помощь при кровотечении из носа", callback_data='bleeding3')],
            [InlineKeyboardButton("Назад в раздел ранений", callback_data='aid_bleeding')],
            [InlineKeyboardButton("Назад в меню первой помощи", callback_data='back_to_menu')],
            [InlineKeyboardButton("Назад в главное меню", callback_data='restart_bot')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        try:
            message = await context.bot.send_video(
                chat_id=chat_id,
                video=open(video_path, 'rb'),
                caption="Нажмите: [здесь](https://29.mchs.gov.ru/deyatelnost/bezopasnost-grazhdan/pervaya-pomoshch-pri-krovotecheniyah), чтобы получить информацию с сайта МЧС России.",
                supports_streaming=True,
                reply_markup=reply_markup,
                parse_mode='Markdown'
            )
        except Exception as e:
            print(f"Ошибка: {e}")
        self.bot.user_message_ids[chat_id].append(message.message_id)

    async def bleeding1_aid_info(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        chat_id = update.effective_chat.id
        query = update.callback_query

        if query:
            await query.answer()
            
        await self.bot.delete_previous_messages(chat_id, context)


        main_text = os.path.join('src', 'first_aid', 'first_aid_text', 'bleeding', 'bleeding1.txt')

        try:
            with open(main_text, 'r', encoding='utf-8') as file:
                main_text = file.read()
        except FileNotFoundError:
            print(f"Файл {main_text} не найден")
        keyboard = [
            [InlineKeyboardButton("Назад в раздел кровотечений", callback_data='bleeding')],
            [InlineKeyboardButton("Назад в раздел ранений", callback_data='aid_bleeding')],
            [InlineKeyboardButton("Назад в меню первой помощи", callback_data='back_to_menu')],
            [InlineKeyboardButton("Назад в главное меню", callback_data='restart_bot')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        message = await context.bot.send_message(chat_id=chat_id, text=main_text, reply_markup=reply_markup, parse_mode='Markdown'
        )
        self.bot.user_message_ids[chat_id].append(message.message_id)

    async def bleeding2_aid_info(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        chat_id = update.effective_chat.id
        query = update.callback_query

        if query:
            await query.answer()
            
        await self.bot.delete_previous_messages(chat_id, context)


        main_text = os.path.join('src', 'first_aid', 'first_aid_text', 'bleeding', 'bleeding2.txt')

        try:
            with open(main_text, 'r', encoding='utf-8') as file:
                main_text = file.read()
        except FileNotFoundError:
            print(f"Файл {main_text} не найден")
        keyboard = [
            [InlineKeyboardButton("В раздел кровотечений", callback_data='bleeding')],
            [InlineKeyboardButton("Назад в раздел ранений", callback_data='aid_bleeding')],
            [InlineKeyboardButton("Назад в меню первой помощи", callback_data='back_to_menu')],
            [InlineKeyboardButton("Назад в главное меню", callback_data='restart_bot')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        message = await context.bot.send_message(chat_id=chat_id, text=main_text, reply_markup=reply_markup, parse_mode='Markdown'
        )
        self.bot.user_message_ids[chat_id].append(message.message_id)

    async def bleeding3_aid_info(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        chat_id = update.effective_chat.id
        query = update.callback_query

        if query:
            await query.answer()
            
        await self.bot.delete_previous_messages(chat_id, context)


        main_text = os.path.join('src', 'first_aid', 'first_aid_text', 'bleeding', 'bleeding3.txt')

        try:
            with open(main_text, 'r', encoding='utf-8') as file:
                main_text = file.read()
        except FileNotFoundError:
            print(f"Файл {main_text} не найден")
        keyboard = [
            [InlineKeyboardButton("Назад в раздел кровотечений", callback_data='bleeding')],
            [InlineKeyboardButton("Назад в раздел ранений", callback_data='aid_bleeding')],
            [InlineKeyboardButton("Назад в меню первой помощи", callback_data='back_to_menu')],
            [InlineKeyboardButton("Назад в главное меню", callback_data='restart_bot')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        message = await context.bot.send_message(chat_id=chat_id, text=main_text, reply_markup=reply_markup, parse_mode='Markdown'
        )
        self.bot.user_message_ids[chat_id].append(message.message_id)


    async def abrasions_aid_info(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        chat_id = update.effective_chat.id
        query = update.callback_query

        if query:
            await query.answer()
            
        await self.bot.delete_previous_messages(chat_id, context)


        main_text = main_text = os.path.join('src', 'first_aid', 'first_aid_text', 'bleeding', 'abrasions.txt')

        try:
            with open(main_text, 'r', encoding='utf-8') as file:
                main_text = file.read()
        except FileNotFoundError:
            print(f"Файл {main_text} не найден")
        keyboard = [
            [InlineKeyboardButton("Назад в раздел ранений", callback_data='aid_bleeding')],
            [InlineKeyboardButton("Назад в меню первой помощи", callback_data='back_to_menu')],
            [InlineKeyboardButton("Назад в главное меню", callback_data='restart_bot')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        message = await context.bot.send_message(chat_id=chat_id, text=main_text, reply_markup=reply_markup, parse_mode='Markdown'
        )
        self.bot.user_message_ids[chat_id].append(message.message_id)

    async def foreign_body_aid_info(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        chat_id = update.effective_chat.id
        query = update.callback_query

        if query:
            await query.answer()
            
        await self.bot.delete_previous_messages(chat_id, context)

        photo_path = os.path.join('src', 'first_aid', 'first_aid_photos', 'foreign_body.jpg')
        message = await context.bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))
        self.bot.user_message_ids[chat_id].append(message.message_id)

        main_text = main_text = os.path.join('src', 'first_aid', 'first_aid_text', 'bleeding', 'foreign_body.txt')

        try:
            with open(main_text, 'r', encoding='utf-8') as file:
                main_text = file.read()
        except FileNotFoundError:
            print(f"Файл {main_text} не найден")
        keyboard = [
            [InlineKeyboardButton("Назад в раздел ранений", callback_data='aid_bleeding')],
            [InlineKeyboardButton("В раздел травмы", callback_data='aid_injury')],
            [InlineKeyboardButton("Назад в меню первой помощи", callback_data='back_to_menu')],
            [InlineKeyboardButton("Назад в главное меню", callback_data='restart_bot')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        message = await context.bot.send_message(chat_id=chat_id, text=main_text, reply_markup=reply_markup, parse_mode='Markdown'
        )
        self.bot.user_message_ids[chat_id].append(message.message_id)

    async def rib_cage_aid_info(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        chat_id = update.effective_chat.id
        query = update.callback_query

        if query:
            await query.answer()
            
        await self.bot.delete_previous_messages(chat_id, context)

        photo_path = os.path.join('src', 'first_aid', 'first_aid_photos', 'rib_cage.jpg')
        message = await context.bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))
        self.bot.user_message_ids[chat_id].append(message.message_id)

        main_text = main_text = os.path.join('src', 'first_aid', 'first_aid_text', 'bleeding', 'rib_cage.txt')

        try:
            with open(main_text, 'r', encoding='utf-8') as file:
                main_text = file.read()
        except FileNotFoundError:
            print(f"Файл {main_text} не найден")
        keyboard = [
            [InlineKeyboardButton("Перелом ребер", callback_data='rib_fracture')],
            [InlineKeyboardButton("Раны с инородным телом", callback_data='foreign_body')],
            [InlineKeyboardButton("Назад в раздел ранений", callback_data='aid_bleeding')],
            [InlineKeyboardButton("Назад в меню первой помощи", callback_data='back_to_menu')],
            [InlineKeyboardButton("Назад в главное меню", callback_data='restart_bot')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        message = await context.bot.send_message(chat_id=chat_id, text=main_text, reply_markup=reply_markup, parse_mode='Markdown'
        )
        self.bot.user_message_ids[chat_id].append(message.message_id)

    async def abdominal_injury_aid_info(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        chat_id = update.effective_chat.id
        query = update.callback_query

        if query:
            await query.answer()
            
        await self.bot.delete_previous_messages(chat_id, context)

        main_text = main_text = os.path.join('src', 'first_aid', 'first_aid_text', 'bleeding', 'abdominal_injury.txt')

        try:
            with open(main_text, 'r', encoding='utf-8') as file:
                main_text = file.read()
        except FileNotFoundError:
            print(f"Файл {main_text} не найден")
        keyboard = [
            [InlineKeyboardButton("Назад в раздел ранений", callback_data='aid_bleeding')],
            [InlineKeyboardButton("Назад в меню первой помощи", callback_data='back_to_menu')],
            [InlineKeyboardButton("Назад в главное меню", callback_data='restart_bot')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        message = await context.bot.send_message(chat_id=chat_id, text=main_text, reply_markup=reply_markup, parse_mode='Markdown'
        )
        self.bot.user_message_ids[chat_id].append(message.message_id)

    async def eye_injuries_aid_info(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        chat_id = update.effective_chat.id
        query = update.callback_query

        if query:
            await query.answer()
            
        await self.bot.delete_previous_messages(chat_id, context)

        main_text = main_text = os.path.join('src', 'first_aid', 'first_aid_text', 'bleeding', 'eye_injuries.txt')

        try:
            with open(main_text, 'r', encoding='utf-8') as file:
                main_text = file.read()
        except FileNotFoundError:
            print(f"Файл {main_text} не найден")
        keyboard = [
            [InlineKeyboardButton("Назад в раздел ранений", callback_data='aid_bleeding')],
            [InlineKeyboardButton("Назад в меню первой помощи", callback_data='back_to_menu')],
            [InlineKeyboardButton("Назад в главное меню", callback_data='restart_bot')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        message = await context.bot.send_message(chat_id=chat_id, text=main_text, reply_markup=reply_markup, parse_mode='Markdown'
        )
        self.bot.user_message_ids[chat_id].append(message.message_id)




