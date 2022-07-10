import logging
import asyncio
import random
import shutil
from datetime import datetime

from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from assets.penguin import photos
from data.config import TOKEN
from keyboards.inline.menu import *
from utils.db_functions.follow_functions import add_follow
from utils.db_functions.requset_functions import get_request
from utils.functions.authentication import authentication_with_start
from utils.functions.image_functions import change_value, get_image
from utils.models.command_functions import *
from utils.db_functions.user_functions import *
from utils.models.commands.boost_command import BoostCommand
from utils.models.commands.credit_command import CreditCommand
from utils.models.commands.help_command import HelpCommand
from utils.models.commands.money_search import MoneySearch
from utils.models.commands.nothing_command import NothingCommand
from utils.models.commands.reduce_command import ReduceCommand
from utils.models.commands.stat_command import StatCommand
from utils.models.context import Context
from utils.models.user import User

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

context = Context()


# handler оf /start command
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    try:
        user = get_user_by_id(message.from_user.id)
        if user.is_admin():
            text = f'Привет, {user.get_name()}. Вы вошли в систему как администратор'
        elif user.is_manager():
            text = f'Привет, {user.get_name()}. Вы вошли в систему как менеджер'
        else:
            text = f'Привет, {user.get_name()}. Я бот, который умеет распозновать деньги на фото'

    except Exception:
        t_id = message.from_user.id
        name = message.from_user.username
        money = 100
        date = datetime.date.today()
        user = User(t_id=t_id, name=name, date=date, money=money)
        add_user(user)
        text = f'Привет, {user.get_name()}. Я бот, который умеет распозновать деньги на фото'
    context.add_user(user, message.chat.id)
    await message.answer(text)


# handler оf /help command
@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    user = authentication_with_start(context, message.from_user, message.chat.id)
    help_cmd = HelpCommand(message.chat.id)
    await help_cmd.execute(user)
    await message.answer(text=help_cmd.message)


# handler оf /menu command
@dp.message_handler(commands=['menu'])
async def send_type(message: types.Message):
    await message.answer(f'Выберите пункт меню', reply_markup=get_menu_kb())


# handler of /boost command
@dp.message_handler(commands=['boost'])
async def send_boost(message: types.Message):
    user = authentication_with_start(context, message.from_user, message.chat.id)
    if user.is_admin():
        command = BoostCommand(message.chat.id)
        text = command.message
        context.set_last_command(user, command)
    else:
        text = NothingCommand(message.chat.id).message
    await message.answer(text)


# handler of /reduce command
@dp.message_handler(commands=['reduce'])
async def send_reduce(message: types.Message):
    user = authentication_with_start(context, message.from_user, message.chat.id)
    if user.is_admin():
        command = ReduceCommand(message.chat.id)
        text = command.message
        context.set_last_command(user, command)
    else:
        text = NothingCommand(message.chat.id).message
    await message.answer(text)


# handler of /stat command
@dp.message_handler(commands=['stat'])
async def send_stat(message: types.Message):
    user = authentication_with_start(context, message.from_user, message.chat.id)
    if user.is_manager() or user.is_admin():
        command = StatCommand(bot, user, message.chat.id)
        context.set_last_command(user, command)
    else:
        command = NothingCommand(message.chat.id)
    text = command.message
    if command.get_menu is None:
        menu = get_none_kb()
    else:
        menu = command.get_menu
    await message.answer(text, reply_markup=menu)


# handler of /id command
@dp.message_handler(commands=['credit'])
async def send_id(message: types.Message):
    user = authentication_with_start(context, message.from_user, message.chat.id)
    if user.is_manager() or user.is_manager():
        command = CreditCommand(message.chat.id)
        context.set_last_command(user, command)
        text = command.message
    else:
        command = NothingCommand(message.chat.id)
        text = command.message
    await message.answer(text)


# handler of /id command
@dp.message_handler(commands=['id'])
async def send_id(message: types.Message):
    await message.answer(f"ваш id: {message.from_user.id}")


# handler of /penguin command
@dp.message_handler(commands=['penguin'])
async def send_id(message: types.Message):
    index = random.randint(0, len(photos) - 1)
    await bot.send_photo(
        photo=photos[index],
        chat_id=message.chat.id)


# handler оf others command
@dp.message_handler(content_types=['photo'])
async def send_photo(message: types.Message):
    user = authentication_with_start(context, message.from_user, message.chat.id)
    command = context.get_last_command(user)
    if isinstance(command, MoneySearch):
        file_info = await bot.get_file(message.photo[-1].file_id)
        path = "assets/images/" + file_info.file_path.split('photos/')[1]
        await message.photo[-1].download(path)
        await command.execute(path)
        await message.answer(command.message)
        if command.is_correct():
            command.save(file_info.file_id)
        if not command.is_script:
            context.set_last_command(user, NothingCommand(message.chat.id))
        shutil.rmtree("assets/images")
        shutil.rmtree("runs/detect")
    else:
        await bot.send_photo(
            photo=message.photo[-1].file_id,
            chat_id=message.chat.id)


# handler of other's text
@dp.message_handler()
async def send_echo(message: types.Message):

    async def get_s_command():
        s_command = get_command(message.text, bot, message.chat.id)
        await s_command.execute(user)
        if s_command.is_script:
            context.set_last_command(user, s_command)
        return s_command

    menu = get_none_kb()
    user = authentication_with_start(context, message.from_user, message.chat.id)
    command = None
    try:
        command = context.get_last_command(user)
        if not isinstance(command, NothingCommand):
            await command.execute(message.text)
            text = command.message
            if not command.is_script:
                context.set_last_command(user, NothingCommand(message.chat.id))
            if command.get_menu is not None:
                menu = command.get_menu
        else:
            command = await get_s_command()
            text = command.message
            if command.get_menu is not None:
                menu = command.get_menu
    except Exception as ex:
        if command is None:
            command = await get_s_command()
            text = command.message
        else:
            text = ex
    await message.reply(text, reply_markup=menu)


# handler of callback like's functuon
@dp.callback_query_handler(text="add_follow")
async def send_like(call: types.CallbackQuery):
    image, user = await get_image(call, bot, context)
    request = get_request(user, image)
    add_follow(request.get_id(), user)
    await call.message.reply("Добавлено в избранное")


# handler of callback like's functuon
@dp.callback_query_handler(text="like")
async def send_like(call: types.CallbackQuery):
    await change_value(call, True, "Я рад, что вам понравилось", bot, context)


# handler of callback dislike's functuon
@dp.callback_query_handler(text="dislike")
async def send_dislike(call: types.CallbackQuery):
    await change_value(call, False, "Я рад, что вам понравилось", bot, context)


async def scheduled(wait_for):
    while True:
        await asyncio.sleep(wait_for)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
