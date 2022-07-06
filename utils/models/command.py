from abc import ABC, abstractmethod

from data.texts.ru_text.command_text import *
from utils.db_functions.requset_functions import get_request
from utils.db_functions.user_functions import *
from utils.models.figure import Circle
from utils.models.figure import figures
from utils.models.request import RequestData
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

    @property
    def is_script(self) -> bool:
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

    @Command.is_script.getter
    def is_script(self) -> bool:
        return True


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

    @Command.is_script.getter
    def is_script(self) -> bool:
        return False


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

    @Command.is_script.getter
    def is_script(self) -> bool:
        return True


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

    @Command.is_script.getter
    def is_script(self) -> bool:
        return True

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

    @Command.is_script.getter
    def is_script(self) -> bool:
        return False


class HistoryCommand(Command):
    """Command for get history of command"""
    _message: str
    _user: User
    _continue = False

    def execute(self, data):
        if isinstance(data, User) and not self._continue:
            self._user = data
            self._continue = True
            self._message = "выберите дату"
        elif data.lower() == "посмотреть полностью" and self._continue:
            try:
                user = self._user
                for request in get_request(user):
                    self._message += request.to_string() + "\n"
            except:
                self._message = "вы еще не делали запросы"
            self._continue = False
        else:
            self._message = "Неправельные данные"

    @Command.message.getter
    def message(self):
        return self._message

    @Command.key_word.getter
    def key_word(self):
        return "история"

    @Command.is_script.getter
    def is_script(self) -> bool:
        return self._continue


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
    _continue = True

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
        self._continue = False

    @Command.message.getter
    def message(self):
        return self._message

    @Command.key_word.getter
    def key_word(self):
        return "boost"

    @Command.is_script.getter
    def is_script(self) -> bool:
        return self._continue


class ReduceCommand(Command):
    """Command for reduce rule of manager"""

    _message = "Введите id пользователя у кого хотите забрать права менеджера"
    _continue = True

    def execute(self, data):
        try:
            t_id = int(data)
            user = User(t_id=t_id)
            result = remove_manager(user)
            if result is None:
                self._message = "Данный пользователь не найден"
            elif result:
                self._message = "Успешно"
            else:
                self._message = "Данный пользователь не является Менеджером"
        except:
            self._message = "Это не id"
        self._continue = False

    @Command.message.getter
    def message(self):
        return self._message

    @Command.key_word.getter
    def key_word(self):
        return "drop"

    @Command.is_script.getter
    def is_script(self) -> bool:
        return self._continue


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

    @Command.is_script.getter
    def is_script(self) -> bool:
        return True


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

    @Command.is_script.getter
    def is_script(self) -> bool:
        return False


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
    """Execute command not according to the script"""
    command = get_command(text)
    command.execute(user)
    return command
