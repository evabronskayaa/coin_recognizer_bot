import logging
import asyncio

from aiogram import Bot, utils, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from data.config import TOKEN
from models.command import get_command
from models.figure import Rectangle, Circle, Triangle

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

figures = [Circle(), Rectangle(), Triangle()]


# handler оf /start command
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer(f'Привет, {message.from_user.first_name}. Я бот, который умеет распозновать монетки на фото')


# handler оf /help command
@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    message_text = f'Ты можешь управлять мною, используя эти команды\n'
    await message.answer(text=message_text)


# handler оf /menu command
@dp.message_handler(commands=['menu'])
async def send_type(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)

    buttons = ['Распознать валюту', 'Избранное', 'История', 'Распознать по слову'] + \
              [f"Распознать на фото {figure.name}и" for figure in figures]
    keyboard.add(*buttons)
    await message.answer(f'Ну давай, выбирай', reply_markup=keyboard)


# handler оf other text
@dp.message_handler()
async def send_echo(message: types.Message):
    text = message.text
    command = get_command(text, figures)

    await message.reply(command.message())


async def scheduled(wait_for):
    while True:
        await asyncio.sleep(wait_for)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(scheduled(10))
    executor.start_polling(dp, skip_updates=True)
