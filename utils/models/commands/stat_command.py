from datetime import datetime, timedelta

from aiogram import Bot
from dateutil import parser

from data.texts.stat_command_text import *
from keyboards.inline.menu import *
from utils.db_functions.stat_functions import get_new_user, get_new_request
from utils.models.Type import Type
from utils.functions.get_chart import build_chart
from utils.models.commands.command import Command
from utils.models.user import User


class StatCommand(Command):
    """Command for get statistics for manager"""

    _message = select_stat
    _type: Type = None
    _continue = True
    _menu = get_stat_kb()
    _start_date = None
    _finish_date = None
    _manual = False
    _bot: Bot = None
    _user: User = None

    def __init__(self, bot, user, chat_id):
        super().__init__(chat_id)
        self._bot = bot
        self._user = user

    async def execute(self, data):
        if self._type is None:
            self._message = select_date
            if data.lower() == for_new_users.lower():
                self._type = Type.USER
                self._menu = get_date_db()
            elif data.lower() == for_new_request.lower():
                self._type = Type.REQUEST
                self._menu = get_date_db()
            else:
                self._message = btn_dont_exist
                self._continue = False
        else:
            self._menu = None
            if data.lower() == self_print.lower() and self._start_date is None and self._finish_date is None:
                self._message = input_start_date
                self._manual = True
            else:
                try:
                    date = parser.parse(data)
                    if self._start_date is None and self._finish_date is None and self._manual:
                        self._start_date = date
                        self._message = input_finish_date

                    elif isinstance(self._start_date, datetime) and self._finish_date is None and self._manual:
                        self._finish_date = date
                        self._continue = False
                        try:
                            await self._execute_stat(self._start_date, self._finish_date)
                        except Exception as ex:
                            self._message = ex.args
                except:
                    if self._manual:
                        self._message = incorrect_date
                    else:
                        if data.lower() == all_time_text.lower():
                            self._continue = False
                            await self._execute_stat()
                        elif data.lower() == last_day_text.lower():
                            start = datetime.today() - timedelta(1)
                            self._continue = False
                            await self._execute_stat(start)
                        else:
                            self._message = btn_dont_exist

    async def _execute_stat(self, start=datetime.min, finish=datetime.today()):
        stat = self._get_stat(start, finish)
        if len(stat) == 0:
            if self._type == Type.USER:
                self._message = havent_users
            elif self._type == Type.REQUEST:
                self._message = havent_requests
        else:
            file = build_chart(stat, self._type)
            await self._bot.send_photo(photo=file, chat_id=self._chat_id)
            self._message = successfully

    def _get_stat(self, start_date, finish_date):
        if self._type == Type.USER:
            return get_new_user(start_date, finish_date)
        elif self._type == Type.REQUEST:
            return get_new_request(start_date, finish_date)

    @Command.message.getter
    def message(self):
        return self._message

    @Command.key_word.getter
    def key_word(self):
        return "/stat"

    @Command.is_script.getter
    def is_script(self) -> bool:
        return self._continue

    @Command.get_menu.getter
    def get_menu(self):
        return self._menu
