from datetime import timedelta, datetime

from dateutil import parser

from data.texts.history_command_text import *
from keyboards.inline.menu import get_date_db, all_time_text, last_day_text, self_print
from utils.db_functions.requset_functions import get_requests
from utils.models.commands.command import Command
from utils.models.user import User


class HistoryCommand(Command):
    """Command for get history of command"""
    _message: str = period
    _user: User
    _continue = True
    _menu = None
    _manual = False
    _start_date = None
    _finish_date = None

    async def execute(self, data):
        if isinstance(data, User):
            self._user = data
            self._message = period
            self._menu = get_date_db()
        else:
            self._menu = None
            if data.lower() == all_time_text.lower():
                self._message = self._get_req_message()
                self._continue = False
            elif data.lower() == last_day_text.lower():
                self._message = self._get_req_message(datetime.today() - timedelta(1))
                self._continue = False
            elif data.lower() == self_print.lower():
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
                        self._message = self._get_req_message(self._start_date, self._finish_date)
                        self._continue = False
                except:
                    if self._manual:
                        self._message = incorrect_date
                    else:
                        self._continue = False
                        self._message = btn_dont_exist

    def _get_req_message(self, start=datetime.min, finish=datetime.today()):
        try:
            user = self._user
            requests = get_requests(user, start, finish)
            if len(requests) > 0:
                text = ""
                for request in requests:
                    text += request.to_string() + "\n\r\n"
                return text
            else:
                return you_havent_follow
        except:
            return error

    @Command.message.getter
    def message(self):
        return self._message

    @Command.key_word.getter
    def key_word(self):
        return "история"

    @Command.is_script.getter
    def is_script(self) -> bool:
        return self._continue

    @Command.get_menu.getter
    def get_menu(self):
        return self._menu
