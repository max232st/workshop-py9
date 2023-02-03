from aiogram import Dispatcher, types
from utils import calc, logwrite

async def calculate(message: types.Message):
    parsed_message = message.text
    logwrite("User input: ", parsed_message)
    temp_list = parsed_message.replace('+', ' + ')\
    .replace('-', ' - ')\
    .replace('*', ' * ')\
    .replace('/', ' / ')\
    .replace('(', '( ')\
    .replace(')', ' )').split()
    temp_list = [int(elem) if elem.isdigit() else elem for elem in temp_list]

    if '(' and ')' in temp_list:
        while '(' in temp_list:
            first_i = len(temp_list) - temp_list[::-1].index('(') - 1
            second_i = first_i + temp_list[first_i + 1:].index(')') + 1
            temp_list = temp_list[:first_i] + calc(temp_list[first_i + 1:second_i]) + temp_list[second_i+1:]

    answer = calc(temp_list)
    logwrite("Solution: ", {answer[0]})
    await message.answer(f"{parsed_message}={answer[0]}")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(calculate)