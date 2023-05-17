from aiogram.dispatcher.filters.state import StatesGroup, State


class CustomerPhone(StatesGroup):
    phone: State = State()


class CustomerStart(StatesGroup):
    start: State = State()
    customer_menu: State = State()
    proposal: State = State()
    orders: State = State()
