from datetime import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext

from bot import bot
from markups.customer_markup import CustomerMarkup
from data.commands import getter, setter
from states import states
from settings.config import KEYBOARD


class CustomerMain:
    @staticmethod
    async def hi_customer(callback: types.CallbackQuery):
        customer = await getter.customer_select(callback.from_user.id)
        if customer is None:
            await bot.delete_message(callback.from_user.id, callback.message.message_id)
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            button = types.KeyboardButton(text='Запрос телефона', request_contact=True)
            keyboard.add(button)
            await bot.send_message(callback.from_user.id,
                                   f"{callback.from_user.first_name}\n"
                                   f"Поделитесь с нами вашим номером телефона!",
                                   reply_markup=keyboard)
            await states.CustomerPhone.phone.set()
        if customer.ban == 0:
            await bot.delete_message(callback.from_user.id, callback.message.message_id)
            await bot.send_message(callback.from_user.id,
                                   f"{callback.from_user.first_name} Спасибо что пользуетесь нашим ботом!",
                                   reply_markup=CustomerMarkup.customer_start())
        if customer.ban == 1:
            await bot.delete_message(callback.from_user.id, callback.message.message_id)
            await bot.send_message(callback.from_user.id, "Вы заблокированы! Обратитесь в техподдержку!")

    @staticmethod
    async def phone(message: types.Message):
        if message.contact.user_id == message.from_user.id:
            res = message.contact.phone_number[-10:]
            await setter.customer_add(message.from_user.id,
                                      message.from_user.username,
                                      f'+7{res}',
                                      message.from_user.first_name,
                                      message.from_user.last_name)
            await bot.send_message(message.from_user.id,
                                   f"{message.from_user.first_name} Спасибо что пользуетесь нашим ботом!",
                                   reply_markup=CustomerMarkup.customer_start())
        else:
            await bot.send_message(message.from_user.id,
                                   "Это не ваш номер телефона! \n"
                                   "Нажмите /start чтобы начать заново")

    @staticmethod
    async def main(callback: types.CallbackQuery):
        await callback.message.edit_text(
                               f"{callback.from_user.first_name} Спасибо что пользуетесь нашим ботом!",
                               reply_markup=CustomerMarkup.customer_start())
