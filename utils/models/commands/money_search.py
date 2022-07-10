from aiogram import Bot
from aiogram.types import InputFile

from money_detector import money_detector
from utils.db_functions.requset_functions import add_request
from utils.db_functions.user_functions import update_user
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
            if data.get_money() <= 5 and not data.is_admin() and not data.is_manager():
                self._continue = False
                self._message = "У вас недостаточно средств"
        else:
            try:
                self._continue = False
                path = data
                money_path, m_message, ach_path = money_detector(path)

                await self._bot.send_photo(
                    photo=InputFile(money_path),
                    chat_id=self._chat_id)
                self._image = open(money_path, "rb").read()
                self._message = m_message
                self._is_correct = True
                self._user.take_money(5)
                print(self._user.get_money())
                update_user(self._user)
            except:
                self._message = "Обьект на фото не найден"

    def save(self, file_id):
        if self._image is not None and self._user is not None:
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
