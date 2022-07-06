from abc import ABC, abstractmethod

from utils.db_functions.requset_functions import get_request
from utils.db_functions.user_functions import add_manager
from utils.models.figure import Circle
from utils.models.figure import figures


class Command(ABC):

    # выполнение команды
    @abstractmethod
    def execute(self, user):
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

    def execute(self, user):
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

    def execute(self, user):
        pass

    @Command.message.getter
    def message(self):
        return 'Моя твоя не понимать'

    @Command.key_word.getter
    def key_word(self):
        return ""


class MoneySearch(Command):
    """Command for search money"""

    def execute(self, user):
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

    def execute(self, user):
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

    def execute(self, user):
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

    def execute(self, user):
        try:
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

    def execute(self, user):
        name = user.get_name()
        money = user.get_money()
        self._message = f"{name}, ваш баланс: {money} баллов"

    @Command.message.getter
    def message(self):
        return self._message

    @Command.key_word.getter
    def key_word(self):
        return "баланс"


class BoostCommand(Command):
    """Command for boost rules for admin"""

    def execute(self, user):
        add_manager(user)

    @Command.message.getter
    def message(self):
        return "Введите id пользователя кому вы хотите выдать права менеджера"

    @Command.key_word.getter
    def key_word(self):
        return "boost"


class ReduceCommand(Command):
    """Command for reduce rule of manager"""

    def execute(self, user):
        add_manager(user)

    @Command.message.getter
    def message(self):
        return "Введите id пользователя у кого хотите забрать права менеджера"

    @Command.key_word.getter
    def key_word(self):
        return "drop"


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
