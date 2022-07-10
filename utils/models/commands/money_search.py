from aiogram import Bot
from aiogram.types import PhotoSize, File, InputFile

from money_detector import money_detector
from utils.db_functions.requset_functions import add_request
from utils.models.commands.command import Command
from utils.models.user import User


class MoneySearch(Command):
    """Command for search money"""
    _message = "Отправьте фотографию"
    _continue = True
    _user: User
    _bot: Bot
    _menu = None
    _image = []

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
                await self._bot.send_photo(
                    photo=money_img,
                    chat_id=self._chat_id)
                self._message = m_message
                self._image = money_img
            except:
                self._message = "Объекты на фото не найдены"

    def save(self, file_id):
        add_request(file_id, self._user, self._message, self._image, False)

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
