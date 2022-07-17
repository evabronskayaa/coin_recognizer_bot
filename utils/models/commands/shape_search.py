from utils.models.commands.command import Command
from utils.models.figure import *


class ShapeSearch(Command):
    """Command for search shapes"""
    _continue = True

    def __init__(self, figure, chat_id):
        super().__init__(chat_id)
        self.__figure = figure
        self._continue = True

    __figure = Circle()

    async def execute(self, data):
        self._continue = False
        # todo search shape

    @Command.message.getter
    def message(self):
        return f'Ждем фотографию с {self.__figure.name}ами'

    @Command.key_word.getter
    def key_word(self):
        return f"Распознать на фото {self.__figure.name.lower()}и"

    @Command.is_script.getter
    def is_script(self) -> bool:
        return self._continue

    @Command.get_menu.getter
    def get_menu(self):
        return None
