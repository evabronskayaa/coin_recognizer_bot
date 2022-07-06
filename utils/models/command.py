from abc import ABC, abstractmethod

from data.texts.ru_text.command_text import *
from utils.db_functions.requset_functions import get_request
from utils.db_functions.user_functions import *
from utils.models.figure import Circle
from utils.models.figure import figures
from utils.models.user import *


class Command(ABC):

    # выполнение команды
    @abstractmethod
    def execute(self, data):
        pass

    # сообщение которое выведет команда с началом работы
    @property
    def message(self) -> str:
        pass

    # ключевое слово по которому мы поймем что нужно выполнить данную команду
    @property
    def key_word(self) -> str:
        pass


class ShapeSearch(Command):
    """Command for search shapes"""

    def __init__(self, figure):
        super().__init__()
        self.__figure = figure

    __figure = Circle()

    def execute(self, data):
        pass
        # todo search shape

    @Command.message.getter
    def message(self):
        return f'ждем фотографию с {self.__figure.name}ами'

    @Command.key_word.getter
    def key_word(self):
        return f"распознать на фото {self.__figure.name.lower()}и"


class NothingCommand(Command):
    """Command that does nothing"""

    def execute(self, data):
        pass

    @Command.message.getter
    def message(self):
        return 'Моя твоя не понимать'

    @Command.key_word.getter
    def key_word(self):
        return ""


class MoneySearch(Command):
    """Command for search money"""

    def execute(self, data):
        pass
        # todo search money

    @Command.message.getter
    def message(self):
        return 'отправляй фотографию'

    @Command.key_word.getter
    def key_word(self):
        return f"загрузить фото"


class OtherSearch(Command):
    """Command for search other objects"""
    _text = ''

    def execute(self, data):
        pass
        # todo search object

    @Command.message.getter
    def message(self):
        return f'ждем фотографию'

    @Command.key_word.getter
    def key_word(self):
        return "распознать по слову"

    # записываем то что будем искать на картинке
    def set_word(self, word):
        self._text = word


class FollowCommand(Command):
    """Command for get follow images"""

    def execute(self, data):
        pass
        # todo print follows

    @Command.message.getter
    def message(self):
        return 'FollowCommand'

    @Command.key_word.getter
    def key_word(self):
        return "избранное"


class HistoryCommand(Command):
    """Command for get history of command"""
    _message: str

    def execute(self, data):
        try:
            user = data
            for request in get_request(user):
                self._message += request.to_string() + "\n"
        except:
            self._message = "вы еще не делали запросы"

    @Command.message.getter
    def message(self):
        return self._message

    @Command.key_word.getter
    def key_word(self):
        return "история"


class CheckMoney(Command):
    """Command for check money of user"""
    _message: str

    def execute(self, data):
        try:
            user = data
            name = user.get_name()
            money = user.get_money()
            self._message = f"{name}, ваш баланс: {money} баллов"
        except:
            self._message = "Техническая ошибка"

    @Command.message.getter
    def message(self):
        return self._message

    @Command.key_word.getter
    def key_word(self):
        return "баланс"


class BoostCommand(Command):
    """Command for boost rules for admin"""

    _message = "Введите id пользователя кому вы хотите выдать права менеджера"

    def execute(self, data):
        try:
            t_id = int(data)
            user = User(t_id=t_id)
            result = add_manager(user)
            if result is None:
                self._message = "Данный пользователь не найден"
            elif result:
                self._message = "Успешно"
            else:
                self._message = "Данный пользователь уже является Менеджером"
        except:
            self._message = "Это не id"

    @Command.message.getter
    def message(self):
        return self._message

    @Command.key_word.getter
    def key_word(self):
        return "boost"


class ReduceCommand(Command):
    """Command for reduce rule of manager"""

    def execute(self, data):
        try:
            t_id = int(data)
            user = User(t_id=t_id)
            result = add_manager(user)
            if result is None:
                self._message = "Данный пользователь не найден"
            elif result:
                self._message = "Успешно"
            else:
                self._message = "Данный пользователь уже является Менеджером"
        except:
            self._message = "Это не id"

    @Command.message.getter
    def message(self):
        return "Введите id пользователя у кого хотите забрать права менеджера"

    @Command.key_word.getter
    def key_word(self):
        return "drop"


class StatCommand(Command):
    """Command for get statistics by manager"""

    def execute(self, user):
        pass

    @Command.message.getter
    def message(self):
        return "Выберте статистику которую хотите узнать"

    @Command.key_word.getter
    def key_word(self):
        return "stat"


class HelpCommand(Command):
    """Command for get help message"""

    _message = " "

    def execute(self, user):
        message_text = help_text
        if isinstance(user, Manager):
            message_text = help_text_manager + """

Выше приведённые команды доступны менеджеру системы"""
        elif isinstance(user, Admin):
            message_text = help_text_admin + """

Выше приведённые команды доступны администратору системы"""
        self._message = message_text

    @Command.message.getter
    def message(self):
        return self._message

    @Command.key_word.getter
    def key_word(self):
        return "help"


def get_commands() -> list[Command]:
    """Function for get all commands"""
    return [FollowCommand(), HistoryCommand(), OtherSearch(),
            MoneySearch(), CheckMoney()] + \
           [ShapeSearch(figure) for figure in figures]


def get_command(text):
    """Get command for text"""
    for command in get_commands():
        if text.lower() in command.key_word.lower():
            return command
    return NothingCommand()


def first_execure(text, user):
    command = get_command(text)
    command.execute(user)
    return command.message
