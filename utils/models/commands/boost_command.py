from utils.db_functions.user_functions import *
from utils.models.commands.command import Command
from data.texts.boost_command_text import *


class BoostCommand(Command):
    """Command for boost rules for admin"""

    _message = default_text
    _continue = True

    def execute(self, data):
        try:
            t_id = int(data)
            result = add_manager_by_id(t_id)
            if result is None:
                self._message = user_not_found
            elif result:
                self._message = successfully
            else:
                self._message = user_is_manager
        except:
            data = data.replace('@', '', 1)
            result = add_manager_by_name(data)
            if result is None:
                self._message = user_not_found
            elif result:
                self._message = successfully
            else:
                self._message = user_is_manager
        self._continue = False

    @Command.message.getter
    def message(self):
        return self._message

    @Command.key_word.getter
    def key_word(self):
        return "/boost"

    @Command.is_script.getter
    def is_script(self) -> bool:
        return self._continue

    @Command.get_menu.getter
    def get_menu(self):
        return None
