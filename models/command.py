from abc import ABC, abstractmethod

from models.figure import Circle


# get command for text
def get_command(text, shapes):
    if 'распознать' in text.lower():
        last_word = text.split(' ')[-1]
        for shape in shapes:
            if shape.name in last_word:
                return ShapeSearch(shape)
        if last_word == 'валюту':
            return MoneySearch()
        elif last_word == 'слову':
            return OtherSearch(last_word)
        return NothingCommand()
    else:
        return NothingCommand()


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @property
    def message(self):
        return ''


# command for search shapes
class ShapeSearch(Command):
    figure = Circle()

    def __init__(self, figure):
        self.figure = figure

    def execute(self):
        pass
        # todo search shape

    def message(self):
        return f'ждем фотографию с {self.figure.name}ами'


# command that does nothing
class NothingCommand(Command):
    def execute(self):
        pass

    def message(self):
        return 'Моя твоя не понимать'


# command for search money
class MoneySearch(Command):
    def execute(self):
        pass
        # todo search money

    def message(self):
        return 'ждем фотографию с деньгами'


# command for search other objects
class OtherSearch(Command):
    text = ''

    def __init__(self, text):
        self.text = text

    def execute(self):
        pass
        # todo search object

    def message(self):
        return f'ждем фотографию с {self.text}'
