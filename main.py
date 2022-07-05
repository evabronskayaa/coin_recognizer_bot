import logging
import asyncio
import utils.models.context

from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from data.config import TOKEN
from keyboards.inline.menu import *
from utils.functions.authentication import authentication
from utils.models.command import *
from utils.db_functions.user_functions import *
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
context = utils.models.context.Context()


# handler оf /start command
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    try:
        user = get_user_by_id(message.from_user.id)
        if check_on_admin(user):
            user = get_admin_by_user(user)
            text = f'Привет, {user.get_name()}. Вы вошли в систему как администратор'
        elif check_on_manager(user):
            user = get_manager_by_user(user)
            text = f'Привет, {user.get_name()}. Вы вошли в систему как менеджер'
        else:
            text = f'Привет, {user.get_name()}. Я бот, который умеет распозновать монетки на фото'

    except Exception:
        t_id = message.from_user.id
        name = message.from_user.first_name
        money = 100
        date = datetime.date.today()
        user = User(t_id=t_id, name=name, date=date, money=money)
        add_user(user)
        text = f'Привет, {user.get_name()}. Я бот, который умеет распозновать монетки на фото'
    context.add_user(user)
    await message.answer(text)


# handler оf /help command
@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    message_text = f'Ты можешь управлять мною, используя эти команды\n'
    await message.answer(text=message_text)


# handler оf /menu command
@dp.message_handler(commands=['menu'])
async def send_type(message: types.Message):
    await message.answer(f'Ну давай, выбирай', reply_markup=get_menu_kb())


# handler of /boost command
@dp.message_handler(commands=['boost'])
async def send_boost(message: types.Message):
    t_id = message.from_user.id
    user = authentication(context, message.from_user)
    if isinstance(user, Admin):
        command = BoostCommand()
        text = command.message
    else:
        text = NothingCommand().message
    await message.answer(text)


# handler оf others command
@dp.message_handler()
async def send_echo(message: types.Message):
    t_id = message.from_user.id
    text = message.text
    if 'ты' in text.lower():
        await message.reply("Да", reply_markup=get_none_kb())
    else:
        command = get_command(text)
        user = authentication(context, message.from_user)
        command.execute(user)
        await message.reply(command.message, reply_markup=get_none_kb())


async def scheduled(wait_for):
    while True:
        await asyncio.sleep(wait_for)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(scheduled(10))
    executor.start_polling(dp, skip_updates=True)