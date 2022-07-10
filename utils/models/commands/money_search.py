from aiogram.types import PhotoSize

from money_detector import money_detector
from utils.models.commands.command import Command
from utils.models.user import User


class MoneySearch(Command):
    """Command for search money"""
    _message = "Отправьте фотографию"
    _continue = True
    _user: User

    async def execute(self, data):
        if isinstance(data, User):
            self._user = data
        elif isinstance(data, PhotoSize):
            self._continue = False
            self._message = "В разработке"
        else:
            raise Exception("incorrect data")
        money_detector(data)

    @Command.message.getter
    def message(self):
        return self._message

    @Command.key_word.getter
    def key_word(self):
        return f"загрузить фото"

    @Command.is_script.getter
    def is_script(self) -> bool:
        return self._continue

    @Command.get_menu.getter
    def get_menu(self):
        return None
