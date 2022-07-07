from enum import Enum

from keyboards.inline.menu import get_date_db
from utils.models.commands.command import Command


class Type(Enum):
    """Emun for check command"""
    USER = 1
    REQUEST = 2


class StatCommand(Command):
    """Command for get statistics by manager"""

    _message = "Выберите статистику которую хотите узнать"
    _type: Type = None
    _continue = True
    _menu = None

    def execute(self, data):
        if self._type is None:
            self._message = "Выбирите дату"
            if data.lower() == 'по новым пользователям':
                self._type = Type.USER
                self._menu = get_date_db()
            elif data.lower() == 'по запросам пользователей':
                self._type = Type.REQUEST
                self._menu = get_date_db()
            else:
                self.message = "Такой кнопки нет"
                self._continue = False
        else:
            self._menu = None
            if data.lower() == "ввести самостоятельно":
                self._message = "Введите дату в формате DD.MM.YYYY или DD/MM/YYYY"
            else:
                self._continue = False

    def _get_stat(self, start_date, finish_date):
        2

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
