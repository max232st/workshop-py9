from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from keyboard import kb_main, kb_in_action
import utils

class FSMInsertData(StatesGroup):
    separator = State()
    info = State()

async def get_separator(message: types.Message):
    await FSMInsertData.separator.set()
    await message.answer("Введите разделитель('-' если запись данных будет разделяться новой строкой в файле)", reply_markup=kb_in_action)

async def save_separator(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['separator'] = message.text
    await FSMInsertData.next()
    await message.answer("Теперь введите данные через ','(ставьте '-' если нет информации)\nПример: Имя, Фамилия, Телефон, Примечание)")

async def insert_data(message: types.Message, state: FSMContext):
    parsed_message = message.text.split(', ')
    async with state.proxy() as data:
        data['info'] = parsed_message
    utils.insert_data(data['info'], data['separator'])
    await message.answer(f"Данные были внесены в справочник", reply_markup=kb_main)
    await state.finish()

async def cancel_action(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply("Действие отменено.", reply_markup=kb_main)

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(get_separator, Text(equals='insert_data', ignore_case=False))
    dp.register_message_handler(cancel_action, Text(equals='cancel', ignore_case=False), state='*')
    dp.register_message_handler(save_separator, state=FSMInsertData.separator)
    dp.register_message_handler(insert_data, state=FSMInsertData.info)