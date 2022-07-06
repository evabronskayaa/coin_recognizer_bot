from utils.models.commands.command import Command
from utils.models.figure import *


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