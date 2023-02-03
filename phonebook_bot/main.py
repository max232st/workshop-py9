import logging
from create_bot import dp
from aiogram import executor
from handlers import start_handler, insert_data_handler, print_data_handler

logging.basicConfig(level=logging.INFO)

start_handler.register_handlers(dp)
insert_data_handler.register_handlers(dp)
print_data_handler.register_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)