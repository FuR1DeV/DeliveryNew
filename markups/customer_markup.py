from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from settings.config import KEYBOARD


class CustomerMarkup:
    @staticmethod
    def main_menu():
        approve_ = InlineKeyboardMarkup()
        get = InlineKeyboardButton(text='Мой профиль',
                                   callback_data='customer_profile')
        get1 = InlineKeyboardButton(text='Создать заказ',
                                    callback_data='customer_create_order')
        approve_.insert(get)
        approve_.insert(get1)
        return approve_

    @staticmethod
    def back_in_main_menu():
        approve_ = InlineKeyboardMarkup()
        back = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} '
                                         f'Вернуться в главное меню',
                                    callback_data='customer_main_menu')
        approve_.insert(back)
        return approve_

    @staticmethod
    def create_order():
        approve_ = InlineKeyboardMarkup(row_width=1)
        send = InlineKeyboardButton(text="Отправить!",
                                    callback_data="customer_send_order")
        back = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} '
                                         f'Вернуться в главное меню',
                                    callback_data='customer_main_menu')
        approve_.insert(send)
        approve_.insert(back)
        return approve_
