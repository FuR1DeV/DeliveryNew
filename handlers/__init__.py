__all__ = ["register_customer"]

from aiogram import Dispatcher
from handlers.customer import CustomerMain
from states import states


def register_customer(disp: Dispatcher):

    """Client Main"""
    disp.register_callback_query_handler(CustomerMain.hi_customer,
                                         state=["*"],
                                         text='customer_start')
    disp.register_message_handler(CustomerMain.phone,
                                  content_types=['contact', 'text'],
                                  state=states.CustomerPhone.phone)
    disp.register_callback_query_handler(CustomerMain.main,
                                         state=["*"],
                                         text="customer_main_menu")
    disp.register_callback_query_handler(CustomerMain.customer_profile,
                                         state=["*"],
                                         text="customer_profile")
    disp.register_callback_query_handler(CustomerMain.customer_create_order,
                                         state=["*"],
                                         text="customer_create_order")
    disp.register_message_handler(CustomerMain.customer_create_order_1,
                                  state=states.CustomerCreateOrder.create_order)
