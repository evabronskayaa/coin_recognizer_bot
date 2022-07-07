from enum import Enum

from utils.models.commands.command import Command


class Type(Enum):
    """Emun for check command"""
    USER = 1
    REQUEST = 2


class StatCommand(Command):
    """Command for get statistics by manager"""

    _message = "Выберте статистику которую хотите узнать"
    _type: Type = None
    _continue = True
    _menu = None

    def execute(self, data):
        if self._type is None:
            self._message = "Выбирите дату"
            if data == 'По новым пользователям':
                self._type = Type.USER
            elif data == 'По запросам пользователей':
                self._type = Type.REQUEST
            else:
                self.message = "Такой кнопки нет"

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
