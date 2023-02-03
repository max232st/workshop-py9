from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_cancel_action = KeyboardButton('cancel')
button_print_data = KeyboardButton('show_data')
button_insert_data = KeyboardButton('insert_data')

kb_main = ReplyKeyboardMarkup(resize_keyboard=True)
kb_main.add(button_insert_data).add(button_print_data)

kb_in_action = ReplyKeyboardMarkup(resize_keyboard=True)
kb_in_action.add(button_cancel_action)
