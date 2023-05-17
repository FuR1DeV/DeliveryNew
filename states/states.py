from aiogram.dispatcher.filters.state import StatesGroup, State


class CustomerPhone(StatesGroup):
    phone: State = State()


class CustomerCreateOrder(StatesGroup):
    create_order: State = State()
