from aiogram import types


def get_menu_kb():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Загрузить фото', 'Избранное', 'История', 'Баланс']
    keyboard.add(*buttons)
    return keyboard


def get_none_kb():
    return types.ReplyKeyboardRemove()