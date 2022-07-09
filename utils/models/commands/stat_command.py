from datetime import datetime, timedelta
from enum import Enum
from dateutil import parser

from keyboards.inline.menu import *
from utils.db_functions.stat_functions import get_new_user, get_new_request
from utils.models.commands.command import Command


class Type(Enum):
    """Emun for check command"""
    USER = 1
    REQUEST = 2


class StatCommand(Command):
    """Command for get statistics by manager"""

    _message = "Выберите статистику, которую хотите узнать"
    _type: Type = None
    _continue = True
    _menu = get_stat_kb()
    _start_date = None
    _finish_date = None
    _manual = False

    def execute(self, data):
        if self._type is None:
            self._message = "Выберите дату"
            if data.lower() == 'по новым пользователям':
                self._type = Type.USER
                self._menu = get_date_db()
            elif data.lower() == 'по запросам пользователей':
                self._type = Type.REQUEST
                self._menu = get_date_db()
            else:
                self._message = "Такой кнопки нет"
                self._continue = False
        else:
            self._menu = None
            if data.lower() == self_print.lower() and self._start_date is None and self._finish_date is None:
                self._message = "Введите дату начала в формате DD.MM.YYYY или DD/MM/YYYY"
                self._manual = True
            else:
                try:
                    date = parser.parse(data)
                    if self._start_date is None and self._finish_date is None and self._manual:
                        self._start_date = date
                        self._message = "Введите дату окончания в формате DD.MM.YYYY или DD/MM/YYYY"

                    elif isinstance(self._start_date, datetime) and self._finish_date is None and self._manual:
                        self._finish_date = date
                        self._continue = False
                        try:
                            self._execute_stat(self._start_date, self._finish_date)
                        except Exception as ex:
                            self._message = ex.args
                except:
                    if self._manual:
                        self._message = "Неправильно введена дата попробуйте еще раз"
                    else:
                        if data.lower() == all_time_text.lower():
                            self._continue = False
                            self._execute_stat()
                        elif data.lower() == last_day_text.lower():
                            start = datetime.today() - timedelta(1)
                            self._continue = False
                            self._execute_stat(start)
                        else:
                            self._message = "Такой кнопки нет"

    def _execute_stat(self, start=datetime.min, finish=datetime.today()):
        stat = self._get_stat(start, finish)
        if len(stat) == 0:
            if self._type == Type.USER:
                self._message = "Новых пользователей за данных период нет"
            elif self._type == Type.REQUEST:
                self._message = "Новых запросов за данных период нет"
        else:
            self._message = "тут будет график"

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
