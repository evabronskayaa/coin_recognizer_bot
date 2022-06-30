from abc import ABC, abstractmethod
import datetime
from models.figure import Circle
from models.figure import figures


# get command for text
def get_command(text):
    date = datetime.date.today()

    for command in commands:
        if text.lower() in command.key_word.lower():
            return command
    return NothingCommand(date)


class Command(ABC):
    date = datetime.date(2012, 12, 14)

    def __init__(self, date):
        self.date = date

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
    __figure = Circle()

    def __init__(self, figure, date):
        super().__init__(date)
        self.figure = figure

    def execute(self):
        pass
        # todo search shape

    @Command.message.getter
    def message(self):
        return f'ждем фотографию с {self.__figure.name}ами'

    @Command.message.getter
    def key_word(self):
        return f"распознать на фото {self.__figure.name.lower()}и"


# command that does nothing
class NothingCommand(Command):
    def execute(self):
        pass

    @Command.message.getter
    def message(self):
        return 'Моя твоя не понимать'

    @Command.message.getter
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

    @Command.message.getter
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

    @Command.message.getter
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

    @Command.message.getter
    def key_word(self):
        return "избранное"


# command for get history of command
class HistoryCommand(Command):

    def execute(self):
        pass
        # todo print history

    @Command.message.getter
    def message(self):
        message = ''
        for command in [ShapeSearch(Circle(), datetime.date.today())]:
            message += f"команда {command.message}\n дата: {command.date}\n"
        return message

    @Command.message.getter
    def key_word(self):
        return "история"


__date = datetime.date.today()
commands = [FollowCommand(__date), HistoryCommand(__date), OtherSearch(__date), MoneySearch(__date)] + \
           [ShapeSearch(figure, __date) for figure in figures]
