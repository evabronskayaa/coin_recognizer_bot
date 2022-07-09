from data.texts.reduce_command_text import *
from utils.db_functions.user_functions import remove_manager_by_id, remove_manager_by_name
from utils.models.commands.command import Command


class ReduceCommand(Command):
    """Command for reduce rule of manager"""

    _message = default_text
    _continue = True

    def execute(self, data):
        try:
            t_id = int(data)
            result = remove_manager_by_id(t_id)
            if result is None:
                self._message = user_not_found
            elif result:
                self._message = successfully
            else:
                self._message = user_isnt_manager
        except:
            data = data.replace('@', '', 1)
            result = remove_manager_by_name(data)
            if result is None:
                self._message = user_not_found
            elif result:
                self._message = successfully
            else:
                self._message = user_isnt_manager
        self._continue = False

    @Command.message.getter
    def message(self):
        return self._message

    @Command.key_word.getter
    def key_word(self):
        return "/reduce"

    @Command.is_script.getter
    def is_script(self) -> bool:
        return self._continue

    @Command.get_menu.getter
    def get_menu(self):
        return None
