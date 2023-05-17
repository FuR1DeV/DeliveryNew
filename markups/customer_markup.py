from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from settings.config import KEYBOARD


class CustomerMarkup:
    @staticmethod
    def customer_start():
        approve_ = InlineKeyboardMarkup()
        get = InlineKeyboardButton(text='Мой профиль',
                                   callback_data='client_profile')
        get1 = InlineKeyboardButton(text='Создать заказ',
                                    callback_data='client_create_order')
        approve_.insert(get)
        approve_.insert(get1)
        return approve_
