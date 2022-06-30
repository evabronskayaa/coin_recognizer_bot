from abc import ABC, abstractmethod
import datetime
from models.figure import Circle


# get command for text
def get_command(text, shapes):
    date = datetime.date.today()
    if 'распознать' in text.lower():
        last_word = text.split(' ')[-1]
        for shape in shapes:
            if shape.name in last_word:
                return ShapeSearch(shape, date)
        if last_word == 'слову':
            return OtherSearch(last_word, date)
        return NothingCommand(date)
    elif 'загрузить фото' in text.lower():
        return MoneySearch(date)
    else:
        return NothingCommand(date)


class Command(ABC):
    data = datetime.date(2012, 12, 14)

    def __init__(self, data):
        self.data = data

    @abstractmethod
    def execute(self):
        pass

    @property
    def message(self):
        pass

    @property
    def key_word(self):
        pass


# command for search shapes
class ShapeSearch(Command):
    figure = Circle()

    def __init__(self, figure, data):
        super().__init__(data)
        self.figure = figure

    def execute(self):
        pass
        # todo search shape

    @Command.message.getter
    def message(self):
        return f'ждем фотографию с {self.figure.name}ами'


# command that does nothing
class NothingCommand(Command):
    def execute(self):
        pass

    @Command.message.getter
    def message(self):
        return 'Моя твоя не понимать'


# command for search money
class MoneySearch(Command):
    def execute(self):
        pass
        # todo search money

    @Command.message.getter
    def message(self):
        return 'отправляй фотографию'


# command for search other objects
class OtherSearch(Command):
    text = ''

    def __init__(self, text, data):
        super().__init__(data)
        self.text = text

    def execute(self):
        pass
        # todo search object

    @Command.message.getter
    def message(self):
        return f'ждем фотографию с {self.text}'


# command for get follow images
class FollowCommand(Command):
    message = ''

    def execute(self):
        pass
        # todo print follows

    @Command.message.getter
    def message(self):
        return self.message


# command for get history of command
class HistoryCommand(Command):
    commands = []

    def execute(self):
        pass
        # todo print history

    @Command.message.getter
    def message(self):
        message = ''
        for command in self.commands:
            message += f'команда {command.message}\n дата: {command.data}\n'
        return self.message
