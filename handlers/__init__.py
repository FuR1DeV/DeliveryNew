__all__ = ["register_customer"]

from aiogram import Dispatcher
from handlers.customer import CustomerMain
from states import states


def register_customer(disp: Dispatcher):

    """Client Main"""
    disp.register_callback_query_handler(CustomerMain.hi_customer,
                                         text='customer_start')
    disp.register_message_handler(CustomerMain.phone,
                                  content_types=['contact', 'text'],
                                  state=states.CustomerPhone.phone)
    disp.register_callback_query_handler(CustomerMain.main,
                                         text="customer_main_menu",
                                         state=["*"])
