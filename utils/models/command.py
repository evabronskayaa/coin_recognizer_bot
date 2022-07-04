from abc import ABC, abstractmethod
import datetime

from utils.models.context import Context
from utils.models.figure import Circle
from utils.models.figure import figures


# function for get all commands
def get_commands(context: Context):
    return [FollowCommand(context), HistoryCommand(context), OtherSearch(context),
            MoneySearch(context), CheckMoney(context)] + \
           [ShapeSearch(figure, context) for figure in figures]


# get command for text
def get_command(text, context: Context):
    for command in get_commands(context):
        if text.lower() in command.key_word.lower():
            return command
    return NothingCommand(context)


class Command(ABC):

    def __init__(self, context: Context):
        self._context = context

    # выполнение команды
    @abstractmethod
    def execute(self):
        pass

    # сообщение которое выведет команда с началом работы
    @property
    def message(self):
        pass

    # ключевое слово по которому мы поймем что нужно выполнить данную команду
    @property
    def key_word(self):
        pass


# command for search shapes
class ShapeSearch(Command):

    def __init__(self, figure, context):
        super().__init__(context)
        self.__figure = figure

    __figure = Circle()

    def execute(self):
        pass
        # todo search shape

    @Command.message.getter
    def message(self):
        return f'ждем фотографию с {self.__figure.name}ами'

    @Command.key_word.getter
    def key_word(self):
        return f"распознать на фото {self.__figure.name.lower()}и"


# command that does nothing
class NothingCommand(Command):

    def execute(self):
        pass

    @Command.message.getter
    def message(self):
        return 'Моя твоя не понимать'

    @Command.key_word.getter
    def key_word(self):
        return ""


# command for search money
class MoneySearch(Command):

    def execute(self):
        pass
        # todo search money

    @Command.message.getter
    def message(self):
        return 'отправляй фотографию'

    @Command.key_word.getter
    def key_word(self):
        return f"загрузить фото"


# command for search other objects
class OtherSearch(Command):
    __text = ''

    def execute(self):
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
        self.__text = word


# command for get follow images
class FollowCommand(Command):
    __text = 'FollowCommand'

    def execute(self):
        pass
        # todo print follows

    @Command.message.getter
    def message(self):
        return self.__text

    @Command.key_word.getter
    def key_word(self):
        return "избранное"


# command for get history of command
class HistoryCommand(Command):

    def execute(self):
        pass
        # todo print history

    @Command.message.getter
    def message(self):
        message = self._context.get_user().get_name()
        return message

    @Command.key_word.getter
    def key_word(self):
        return "история"


# command for check money by user
class CheckMoney(Command):
    _message: str

    def execute(self):
        user = self._context.get_user()
        name = user.get_name()
        money = user.get_money()
        self._message = f"{name}, ваш баланс: {money}"

    @Command.message.getter
    def message(self):
        return self._message

    @Command.key_word.getter
    def key_word(self):
        return "баланс"
