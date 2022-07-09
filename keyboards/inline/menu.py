from aiogram import types
from aiogram.types import KeyboardButton

load_photo = 'Загрузить фото'
follow = 'Избранное'
history = 'История'
balance = 'Баланс'


def get_menu_kb():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = [load_photo, follow, history, balance]
    keyboard.add(*buttons)
    return keyboard


def get_none_kb():
    return types.ReplyKeyboardRemove()


for_new_users = 'По запросам пользователей'
for_new_request = 'По новым пользователям'


def get_stat_kb():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = [for_new_request, for_new_users]
    keyboard.add(*buttons)
    return keyboard


all_time_text = 'Все время'
last_day_text = 'Последний день'
self_print = 'Ввести самостоятельно'


def get_date_db():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn = KeyboardButton(self_print)
    buttons = [all_time_text, last_day_text]
    keyboard.row(*buttons).add(btn)
    return keyboard


top_up = "Пополнить"


def get_balance_kb():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = [top_up]
    keyboard.add(*buttons)
    return keyboard
