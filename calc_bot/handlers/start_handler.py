from aiogram import Dispatcher, types

async def help(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name}!\nДля работы с ботом просто введите пример в чат\nПример: (1.5+1.5)*2")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(help, commands=['start', 'help'])
