import os
import json
import shutil

import asyncio
from datetime import datetime

import aioschedule
from aiogram import types, executor
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext

from bot import dp, bot
from data.commands import setter, getter
from data.db_gino import db
from handlers import register_customer
from markups.admin_markup import AdminMarkup
# from handlers import register_admin_handler, register_client_handler
# from markups.client_markup import ClientMarkup
# from markups.admin_markup import AdminMarkup
from settings.config import KEYBOARD, ADMIN_ID


@dp.message_handler(commands='start', state='*')
async def start(message: types.Message, state: FSMContext):
    await state.finish()
    await bot.send_message(message.from_user.id,
                           f'<b>Приветствуем!</b>\n\n'
                           f'<b>Вы Курьер или Заказчик ?</b> <i>{message.from_user.first_name} ?</i>',
                           reply_markup=AdminMarkup.clients_start())


# @dp.message_handler(Command("admin"), state=["*"])
# async def admin(message: types.Message, state: FSMContext):
#     await state.finish()
#     if str(message.from_user.id) in ADMIN_ID:
#         admin_ = await getter.admin_select(message.from_user.id)
#         if not admin_:
#             await setter.admin_add(message.from_user.id,
#                                    message.from_user.username)
#         await bot.send_message(message.from_user.id,
#                                "<b>Добро пожаловать в меню Администратора</b>\n\n"
#                                "<b>Вы можете просмотреть cписок пользователей, "
#                                "список связей, найти пользователя, изменения лимитов.</b>\n\n",
#                                reply_markup=AdminMarkup.admin_menu())
#     else:
#         await bot.send_message(message.from_user.id, "У вас нет прав доступа!")
#


# async def scheduler():
#     aioschedule.every().second.do(check_subscribe)
#     while True:
#         await aioschedule.run_pending()
#         await asyncio.sleep(30)


async def on_startup(_):
    from data import db_gino
    print("Database connected")
    await db_gino.on_startup(dp)
    # asyncio.create_task(scheduler())
    """Удалить БД"""
    # await db.gino.drop_all()

    """Создание БД"""
    await db_gino.db.gino.create_all()

    """Регистрация хэндлеров"""
    # register_admin_handler(dp)
    register_customer(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
