import logging

from data.models.customers import Customers

logger = logging.getLogger("bot.data.commands.customer_set_db")

"""Функции добавления/обновления БД для Заказчика"""


async def customer_add(user_id, username, telephone, first_name, last_name):
    """Заказчик добавляется в БД"""
    customer = Customers(user_id=user_id, username=username, telephone=telephone, first_name=first_name,
                         last_name=last_name)
    await customer.create()
