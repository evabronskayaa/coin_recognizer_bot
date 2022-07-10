from aiogram import Bot
from aiogram.types import InputFile

from keyboards.inline.menu import get_follow_inline_kb, get_arhiv_kb, yes, no
from money_detector import money_detector
from utils.db_functions.requset_functions import add_request
from utils.db_functions.user_functions import update_user
from utils.models.commands.command import Command
from utils.models.user import User


class MoneySearch(Command):
    """Command for search money"""
    _message = "Для удовлетворительного результата нужна фотография в хорошем качестве, " \
               "на контрастном для объектов фоне, желательно снимать близко к объектам"
    _continue = True
    _user: User = None
    _bot: Bot
    _menu = None
    _image = None
    _is_correct = False
    _m_message = ""
    _is_photo = True
    _arhiv = None

    def __init__(self, chat_id, bot):
        self._bot = bot
        super().__init__(chat_id)

    async def execute(self, data):
        if isinstance(data, User):
            self._user = data
            if data.get_money() <= 5 and not data.is_admin() and not data.is_manager():
                self._continue = False
                self._message = "У вас недостаточно средств"
        elif self._is_photo:
            try:
                path = data
                money_path, m_message, ach_path = money_detector(path)

                await self._bot.send_photo(
                    photo=InputFile(money_path),
                    chat_id=self._chat_id, reply_markup=get_follow_inline_kb())
                self._image = open(money_path, "rb").read()
                self._arhiv = ach_path
                self._m_message = m_message
                self._message = m_message + "\n\n" + "Желаете получить архив?"
                self._is_correct = True
                self._is_photo = False
                self._user.take_money(5)
                self._menu = get_arhiv_kb()
                update_user(self._user)
            except:
                self._message = "Объект на фото не найден"
                self._continue = False
        else:
            if self._is_correct and self._arhiv is not None:
                if data.lower() == yes.lower():
                    self._message = "вот, архив"
                    arg = open(self._arhiv, "rb")
                    await self._bot.send_document(document=arg, chat_id=self._chat_id)
                    self._continue = False
                    self._menu = None
                elif data.lower() == no.lower():
                    self._message = "как, скажите"
                    self._continue = False
                    self._menu = None
                else:
                    "Такой кнопки нет"
                    self._continue = False
            else:
                raise Exception("incorrect data")

    def save(self, file_id):
        if self._image is not None and self._user is not None:
            add_request(file_id, self._user, self._m_message, self._image)

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
