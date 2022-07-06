import logging
import asyncio

import utils.models.context

from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from data.config import TOKEN
from keyboards.inline.menu import *
from utils.functions.authentication import authentication_with_start
from utils.models.context import *
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
    user = authentication_with_start(context, message.from_user)
    help_cmd = HelpCommand()
    help_cmd.execute(user)
    await message.answer(text=help_cmd.message)


# handler оf /menu command
@dp.message_handler(commands=['menu'])
async def send_type(message: types.Message):
    await message.answer(f'Ну давай, выбирай', reply_markup=get_menu_kb())


# handler of /boost command
@dp.message_handler(commands=['boost'])
async def send_boost(message: types.Message):
    user = authentication_with_start(context, message.from_user)
    if isinstance(user, Admin):
        command = BoostCommand()
        text = command.message
        context.set_last_command(user, command)
        print("send")
    else:
        text = NothingCommand().message
    await message.answer(text)


# handler of /reduce command
@dp.message_handler(commands=['reduce'])
async def send_reduce(message: types.Message):
    user = authentication_with_start(context, message.from_user)
    if isinstance(user, Admin):
        command = ReduceCommand()
        text = command.message
    else:
        text = NothingCommand().message
    await message.answer(text)


# handler of /stat command
@dp.message_handler(commands=['stat'])
async def send_reduce(message: types.Message):
    user = authentication_with_start(context, message.from_user)
    if isinstance(user, Admin) | isinstance(user, Manager):
        command = StatCommand()
        text = command.message
    else:
        text = NothingCommand().message
    await message.answer(text, reply_markup=get_stat_kb())


# handler of /id command
@dp.message_handler(commands=['id'])
async def send_reduce(message: types.Message):
    await message.answer(message.from_user.id, reply_markup=get_stat_kb())


# handler оf others command
@dp.message_handler(content_types=['photo'])
async def handle_docs_photo(message: types.Message):
    await bot.send_photo(photo='https://risovach.ru/upload/2013/10/mem/a-huy-tebe_33321944_orig_.jpeg',
                         chat_id=message.chat.id)


# handler of other's text
@dp.message_handler()
async def send_echo(message: types.Message):
    user = authentication_with_start(context, message.from_user)
    try:
        command = context.get_last_command(user)
        text = script_execute_command(message.text, command, context)
    except:
        command = get_command(message.text)
        command.execute(user)
        text = command.message
    await message.reply(text, reply_markup=get_none_kb())


async def scheduled(wait_for):
    while True:
        await asyncio.sleep(wait_for)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
