from aiogram import types
from aiogram.types import KeyboardButton


def get_menu_kb():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ['Загрузить фото', 'Избранное', 'История', 'Баланс']
    keyboard.add(*buttons)
    return keyboard


def get_none_kb():
    return types.ReplyKeyboardRemove()


def get_stat_kb():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ['По новым пользователям', 'По запросам пользователей']
    keyboard.add(*buttons)
    return keyboard


all_time_text = 'Все время'
last_day_text = 'Последний день'
self_print = 'Ввести самостоятельно'


def get_date_db():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn = KeyboardButton('Ввести самостоятельно')
    buttons = ['Все время', 'Последний день']
    keyboard.row(*buttons).add(btn)
    return keyboard
