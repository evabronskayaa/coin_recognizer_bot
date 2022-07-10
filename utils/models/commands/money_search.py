from aiogram import Bot
from aiogram.types import InputFile

from money_detector import money_detector
from utils.db_functions.requset_functions import add_request
from utils.models.commands.command import Command
from utils.models.user import User


class MoneySearch(Command):
    """Command for search money"""
    _message = "Отправьте фотографию"
    _continue = True
    _user: User = None
    _bot: Bot
    _menu = None
    _image = None
    _is_correct = False

    def __init__(self, chat_id, bot):
        self._bot = bot
        super().__init__(chat_id)

    async def execute(self, data):
        if isinstance(data, User):
            self._user = data
        else:
            self._continue = False
            try:
                path = data
                money_img, m_message, ach_path = money_detector(path)
                self._image = money_img.read()
                money_img.close()
                result = InputFile(money_img)
                await self._bot.send_photo(
                    photo=result,
                    chat_id=self._chat_id)
                self._message = m_message
                self._is_correct = True
            except:
                self._message = "Объекты на фото не найдены"

    def save(self, file_id):
        if self._image is not None and self._user is not None:
            print(self._image)
            add_request(file_id, self._user, self._message, self._image)

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
        return self._menu

    def is_correct(self):
        return self._is_correct
