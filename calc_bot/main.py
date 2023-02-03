import logging
from create_bot import dp
from aiogram import executor
from handlers import start_handler, calculate_handler

logging.basicConfig(level=logging.INFO)

start_handler.register_handlers(dp)
calculate_handler.register_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)