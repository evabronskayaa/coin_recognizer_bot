from utils.db_functions.follow_functions import get_follows
from utils.models.commands.command import Command
from aiogram import Bot

from utils.models.user import User


class FollowCommand(Command):
    """Command for get follow images"""
    _message = "suck"
    _bot: Bot = None

    def __init__(self, bot):
        self._bot = bot

    def execute(self, data):
        if isinstance(data, User):
            user = data
            requests = get_follows(user)
            if len(requests) > 0:
                self._message = "Держи"
                for request in requests:
                    try:
                        self._bot.send_photo(chat_id=user.get_id(), photo=request.get_id())
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
