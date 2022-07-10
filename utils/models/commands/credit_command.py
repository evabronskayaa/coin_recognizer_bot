from data.texts.credit_command_text import *
from utils.db_functions.user_functions import get_user_by_id, get_user_by_name, update_user
from utils.models.commands.command import Command


class CreditCommand(Command):
    """Command for get follow images"""
    _message = default_text
    _continue = True
    _user = None

    async def execute(self, data):
        try:
            t_id = int(data)
            try:
                self._user = get_user_by_id(t_id)
                self._message = top_up
            except:
                if self._user is None:
                    self._message = user_not_found
                    self._continue = False
                else:
                    self._user.add_money(t_id)
                    update_user(self._user)
                    self._message = successfully
                    self._continue = False
        except:
            data = data.replace('@', '', 1)
            try:
                self._user = get_user_by_name(data)
                self._message = top_up
            except:
                self._continue = False
                if self._user is None:
                    self._message = user_not_found
                else:
                    self._message = isnt_int

    @Command.message.getter
    def message(self):
        return self._message

    @Command.key_word.getter
    def key_word(self):
        return "credit"

    @Command.is_script.getter
    def is_script(self) -> bool:
        return self._continue

    @Command.get_menu.getter
    def get_menu(self):
        return None
