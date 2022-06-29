from abc import ABC, abstractmethod

from models.figure import Circle


# get command for text
def get_command(text, shapes):
    if 'распознать' in text.lower():
        last_word = text.split(' ')[-1]
        for shape in shapes:
            if shape.name in last_word:
                ShapeSearch(shape)
        if last_word == 'валюту':
            MoneySearch()
        elif last_word == 'слову':
            OtherSearch(last_word)
        NothingCommand()
    else:
        NothingCommand()


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @property
    def message(self):
        ''


# command for search shapes
class ShapeSearch(Command):
    figure = Circle()

    def __init__(self, figure):
        self.figure = figure

    def execute(self):
        pass
        # todo search shape

    def message(self):
        f'ждем фотографию с {self.figure.name}ами'


# command that does nothing
class NothingCommand(Command):
    def execute(self):
        pass

    def message(self):
        'Моя твоя не понимать'


# command for search money
class MoneySearch(Command):
    def execute(self):
        pass

    def message(self):
        'ждем фотографию с деньгами'


# command for search other objects
class OtherSearch(Command):
    text = ''

    def __init__(self, text):
        self.text = text

    def execute(self):
        pass
        # todo search shape

    def message(self):
        f'ждем фотографию с {self.text}'
