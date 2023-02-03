from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text
import utils

async def show_data(message: types.Message):
    data = utils.export_data()
    if len(data) > 0:
        for item in data:
            await message.answer(f'''
Фамилия: {item[0]}    
Имя: {item[1]}
Телефон: {item[2]}    
Примечание: {item[3]}\n
            ''')
    else:
        print("В справочнике нет данных!")
    
def register_handlers(dp: Dispatcher):
    dp.register_message_handler(show_data, Text(equals='show_data', ignore_case=False))
