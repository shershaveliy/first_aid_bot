from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler
import os

from first_aid.Reanimation import ReanimationAid
from first_aid.injury import InjuryAid
from first_aid.bleeding import BleedingAid
from first_aid.head_and_back import Head_and_back
from first_aid.burns import Burns
from first_aid.breath import Breath
from first_aid.heat_stroke import Heat_stroke
from first_aid.poisoning import Poisoning
from first_aid.bites import Bites


from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from main import MyBot

class FirstAid:
    def __init__(self, my_bot: "MyBot"):
        self.bot = my_bot
        self.app = my_bot.app
        self.reanimation_aid = ReanimationAid(my_bot, self)
        self.injury_aid = InjuryAid(my_bot, self)
        self.bleeding_aid = BleedingAid(my_bot, self)
        self.head_and_back = Head_and_back(my_bot, self)
        self.burns = Burns(my_bot, self)
        self.breath = Breath(my_bot, self)
        self.heat_stroke = Heat_stroke(my_bot, self)
        self.poisoning = Poisoning(my_bot, self)
        self.bites = Bites(my_bot, self)
        self.register_handlers()  # Регистрируем обработчики при инициализации
    
    
    def register_handlers(self):
        # Регистрируем обработчики для меню первой помощи и кнопок
        #self.app.add_handler(CommandHandler("start", self.start))
        self.app.add_handler(CommandHandler("first_aid", self.first_aid_menu))
        self.app.add_handler(CallbackQueryHandler(self.reanimation_aid.provide_reanimation_aid_info, pattern='^aid_reanimation$'))
        self.app.add_handler(CallbackQueryHandler(self.injury_aid.provide_injury_aid_info, pattern='^aid_injury$'))
        self.app.add_handler(CallbackQueryHandler(self.bleeding_aid.main_provide_bleeding_aid_info, pattern='^aid_bleeding$'))
        self.app.add_handler(CallbackQueryHandler(self.head_and_back.main_head_and_back_aid_info, pattern='^head_and_back$'))
        self.app.add_handler(CallbackQueryHandler(self.burns.main_burns_aid_info, pattern='^burns$'))
        self.app.add_handler(CallbackQueryHandler(self.breath.main_breath_aid_info, pattern='^breath$'))
        self.app.add_handler(CallbackQueryHandler(self.heat_stroke.main_heat_stroke_aid_info, pattern='^heat_stroke$'))
        self.app.add_handler(CallbackQueryHandler(self.poisoning.main_poisoning_aid_info, pattern='^poisoning$'))
        self.app.add_handler(CallbackQueryHandler(self.bites.main_bites_aid_info, pattern='^bites$'))
        self.app.add_handler(CallbackQueryHandler(self.first_aid_menu, pattern='^back_to_menu$'))
        self.app.add_handler(CallbackQueryHandler(self.bot.start, pattern='^restart_bot$'))



    async def first_aid_menu(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        chat_id = update.effective_chat.id
        query = update.callback_query
        if query:
            await query.answer()

        await self.bot.delete_previous_messages(chat_id, context)
        # Меню первой помощи с вариантами
        keyboard = [
            [InlineKeyboardButton("Реанимация (СЛР)", callback_data='aid_reanimation')],
            [InlineKeyboardButton("Ранения/кровотечение/порезы", callback_data='aid_bleeding')],
            [InlineKeyboardButton("Травмы (переломы/вывихи/растяжения)", callback_data='aid_injury')],
            [InlineKeyboardButton("Ожоги/химические ожоги", callback_data='burns')],
            [InlineKeyboardButton("Травмы головы и позвоночника", callback_data='head_and_back')],
            [InlineKeyboardButton("Непроходимость дыхательных путей", callback_data='breath')],
            [InlineKeyboardButton("Первая помощь при тепловом ударе", callback_data='heat_stroke')],
            [InlineKeyboardButton("Отравления", callback_data='poisoning')],
            [InlineKeyboardButton("Укусы/укусы змеи", callback_data='bites')],
            [InlineKeyboardButton("Назад в главное меню", callback_data='restart_bot')],

        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        welcome_message = (
            "*Добро пожаловать в Бот Экстренной Помощи!* 🚑\n\n"
            "Этот бот поможет вам быстро получить информацию и рекомендации по оказанию первой помощи в экстренных ситуациях. "
            "Помните, что от своевременных действий может зависеть жизнь человека. Вот что умеет наш бот:\n\n"
            
            "📋 *Меню помощи*:\n\n"
            "- Узнайте, как действовать при ожогах, кровотечениях, травмах и других ситуациях.\n"
            "- Получите пошаговые инструкции по реанимации и сердечно-легочной помощи.\n\n"
            
            "📞 *Экстренные номера*:\n\n"
            "- Позвоните в экстренную службу по номеру: *112*.\n"
            "- Вызвать скорую медицинскую помощь по номеру: *103*.\n\n"
            
            "❗ *Важно!*\n\n"
            "Этот бот создан для информационной поддержки. В критической ситуации обязательно вызывайте профессиональных спасателей "
            "или скорую помощь по номеру *112*.\n\n"

            "Информация взята с [сайта МЧС России](https://mchs.gov.ru/deyatelnost/bezopasnost-grazhdan#safety-11)\n\n"
            
            "Нажмите кнопку ниже, чтобы начать"
        )

        message = await context.bot.send_message(
            chat_id=chat_id,
            text=welcome_message,
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
        self.bot.user_message_ids.setdefault(chat_id, []).append(message.message_id)

