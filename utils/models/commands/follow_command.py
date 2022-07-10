from aiogram.types import InputFile

from keyboards.inline.menu import get_remove_inline_kb
from utils.db_functions.follow_functions import get_follows
from utils.models.commands.command import Command
from aiogram import Bot
import io

from utils.models.user import User


class FollowCommand(Command):
    """Command for get follow images"""
    _message = "хе-хе"
    _bot: Bot = None

    def __init__(self, bot, chat_id):
        super().__init__(chat_id)
        self._bot = bot

    async def execute(self, data):
        if isinstance(data, User):
            user = data
            requests = get_follows(user)
            if len(requests) > 0:
                self._message = "Держи"
                for request in requests:
                    try:
                        image = InputFile(io.BytesIO(request.get_images_bytes()))
                        await self._bot.send_photo(chat_id=self._chat_id, photo=image,
                                                   reply_markup=get_remove_inline_kb())
                        await self._bot.send_message(chat_id=self._chat_id, text=request.get_message())
                    except:
                        self._message = "хм"
            else:
                self._message = "У вас нет избраного"
        else:
            self._message = "Что-то пошло не так"

    @Command.message.getter
    def message(self):
        return self._message

    @Command.key_word.getter
    def key_word(self):
        return "избранное"

    @Command.is_script.getter
    def is_script(self) -> bool:
        return False

    @Command.get_menu.getter
    def get_menu(self):
        return None
