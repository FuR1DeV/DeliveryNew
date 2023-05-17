from sqlalchemy import and_

from data.models.customers import Customers


"""Функции взятия информации из БД для Заказчика"""


async def customer_select(user_id):
    customer = await Customers.query.where(Customers.user_id == user_id).gino.first()
    return customer
