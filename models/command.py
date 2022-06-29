from abc import ABC, abstractmethod

from models.figure import Circle


# get command for text
def get_command(text, shapes):
    if 'распознать' in text.lower():
        last_word = text.split(' ')[-1]
        for shape in shapes:
            if shape.name in last_word:
                ShapeSearch(shape)
        NothingCommand()
    else:
        NothingCommand()


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @property
    def message(self):
        pass


# command for search shapes

class ShapeSearch(Command):
    figure = Circle()

    def __init__(self, figure):
        self.figure = figure

    def execute(self):
        var = ()
        # todo search shape

    def message(self):
        f"ждем фотографию с {self.figure.name}ами"


# command that does nothing
class NothingCommand(Command):
    def execute(self):
        var = ()

    def message(self):
        "Моя твоя не понимать"
