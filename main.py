import logging
import asyncio

from aiogram import Bot, Dispatcher, executor, utils, types
from data.config import TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer(f'Привет, {message.from_user.first_name}. Я бот, который умеет распозновать монетки на фото')


@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    message_text = f'Ты можешь управлять мною, используя эти команды\n'
    await message.answer(text=message_text)


@dp.message_handler(commands=['menu'])
async def send_type(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Отправить фото', 'Избранное', 'История']
    keyboard.add(*buttons)
    await message.answer(f'Ну давай, выбирай', reply_markup=keyboard)


# @dp.message_handler(Text(equals='Отправить фото'))
# async def get_photo(message: types.Message):
#     await message.reply('')


async def scheduled(wait_for):
    while True:
        await asyncio.sleep(wait_for)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(scheduled(10))
    executor.start_polling(dp, skip_updates=True)
    a = 6
    t = 4


