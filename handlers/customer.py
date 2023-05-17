from aiogram import types
from aiogram.dispatcher import FSMContext

from bot import bot
from markups.customer_markup import CustomerMarkup
from markups.performer_markup import PerformerMarkup
from data.commands import getter, setter
from states import states


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
        elif customer.ban == 0:
            await callback.message.edit_text(f"{callback.from_user.first_name} Спасибо что пользуетесь нашим ботом!",
                                             reply_markup=CustomerMarkup.main_menu())
        elif customer.ban == 1:
            await callback.message.edit_text(f"{callback.from_user.first_name} "
                                             f"Вы заблокированы! Обратитесь в техподдержку!",
                                             reply_markup=CustomerMarkup.main_menu())

    @staticmethod
    async def phone(message: types.Message):
        if message.contact.user_id == message.from_user.id:
            res = message.contact.phone_number[-10:]
            await setter.customer_add(message.from_user.id,
                                      message.from_user.username,
                                      f'+7{res}',
                                      message.from_user.first_name,
                                      message.from_user.last_name)
            await bot.delete_message(message.from_user.id, message.message_id)
            await bot.delete_message(message.from_user.id, message.message_id - 1)
            await bot.send_message(message.from_user.id,
                                   f"{message.from_user.first_name} Спасибо что пользуетесь нашим ботом!",
                                   reply_markup=CustomerMarkup.main_menu())
        else:
            await bot.send_message(message.from_user.id,
                                   "Это не ваш номер телефона! \n"
                                   "Нажмите /start чтобы начать заново")

    @staticmethod
    async def main(callback: types.CallbackQuery):
        await callback.message.edit_text(
            f"{callback.from_user.first_name} Спасибо что пользуетесь нашим ботом!",
            reply_markup=CustomerMarkup.main_menu())

    @staticmethod
    async def customer_profile(callback: types.CallbackQuery):
        customer = await getter.customer_select(callback.from_user.id)
        await callback.message.edit_text(
            f"У вас создано заказов - {customer.created_orders}\n"
            f"Отменено заказов - {customer.canceled_orders}",
            reply_markup=CustomerMarkup.back_in_main_menu())

    @staticmethod
    async def customer_create_order(callback: types.CallbackQuery):
        await callback.message.edit_text("Опишите ваш заказ\n\n"
                                         "<b>Пример:</b> \n"
                                         "<i>Добрый вечер!</i>\n\n"
                                         "<i>Забрать: Суперметалл, 2-я Бауманская, 9/23 с 3</i>\n"
                                         "<i>Отвезти: Паршина, 10</i>\n\n"
                                         "<i>650 руб</i>\n\n"
                                         "<b>Напишите и отправьте мне!</b>\n"
                                         "<i>Или можете вернуться в главное меню</i>",
                                         reply_markup=CustomerMarkup.back_in_main_menu())
        await states.CustomerCreateOrder.create_order.set()

    @staticmethod
    async def customer_create_order_1(message: types.Message, state: FSMContext):
        result = message.text
        await bot.delete_message(message.from_user.id, message.message_id)
        await bot.delete_message(message.from_user.id, message.message_id - 1)
        await bot.send_message(message.from_user.id,
                               "Вы ваш заказ выглядит так:\n\n"
                               f"{result}",
                               reply_markup=CustomerMarkup.create_order())
        async with state.proxy() as data:
            data["order"] = result

    @staticmethod
    async def customer_send_order(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            order = data.get("order")
            await bot.send_message("@FlowWorkDeliveryGroup",
                                   f"{order}",
                                   reply_markup=PerformerMarkup.performer_start())
        await callback.message.edit_text("Вы отправили заказ в группу!",
                                         reply_markup=CustomerMarkup.main_menu())
