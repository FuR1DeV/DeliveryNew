from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from settings.config import KEYBOARD


class PerformerMarkup:
    @staticmethod
    def performer_start():
        approve_ = InlineKeyboardMarkup()
        get1 = InlineKeyboardButton(text='Взять заказ',
                                    callback_data='performer_get_order')
        approve_.insert(get1)
        return approve_
