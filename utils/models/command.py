from abc import ABC, abstractmethod

from utils.db_functions.requset_functions import get_request
from utils.models.figure import Circle
from utils.models.figure import figures


# function for get all commands
def get_commands():
    return [FollowCommand(), HistoryCommand(), OtherSearch(),
            MoneySearch(), CheckMoney()] + \
           [ShapeSearch(figure) for figure in figures]


# get command for text
def get_command(text):
    for command in get_commands():
        if text.lower() in command.key_word.lower():
            return command
    return NothingCommand()


class Command(ABC):

    # выполнение команды
    @abstractmethod
    def execute(self, user):
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


# command that does nothing
class NothingCommand(Command):

    def execute(self, t_id):
        pass

    @Command.message.getter
    def message(self, user):
        return 'Моя твоя не понимать'

    @Command.key_word.getter
    def key_word(self):
        return ""


# command for search money
class MoneySearch(Command):

    def execute(self, user):
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


# command for get follow images
class FollowCommand(Command):

    def execute(self, user):
        pass
        # todo print follows

    @Command.message.getter
    def message(self):
        return 'FollowCommand'

    @Command.key_word.getter
    def key_word(self):
        return "избранное"


# command for get history of command
class HistoryCommand(Command):
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


# command for check money by user
class CheckMoney(Command):
    _message: str

    def execute(self, user):
        name = user.get_name()
        money = user.get_money()
        self._message = f"{name}, ваш баланс: {money}"

    @Command.message.getter
    def message(self):
        return self._message

    @Command.key_word.getter
    def key_word(self):
        return "баланс"
