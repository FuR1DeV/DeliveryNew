from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from settings.config import KEYBOARD


class AdminMarkup:
    @staticmethod
    def clients_start():
        approve_ = InlineKeyboardMarkup()
        start_1 = InlineKeyboardButton(text='Я Заказчик',
                                       callback_data='customer_start')
        start_2 = InlineKeyboardButton(text='Я Курьер',
                                       callback_data='performer_start')
        approve_.insert(start_1)
        approve_.insert(start_2)
        return approve_
