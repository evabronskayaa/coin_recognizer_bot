from data.texts.ru_text.command_text import *
from utils.models.commands.command import Command
from utils.models.user import *


class HelpCommand(Command):
    """Command for get help message"""

    _message = " "

    def execute(self, user):
        message_text = help_text
        if isinstance(user, Manager):
            message_text = help_text_manager + """

Выше приведённые команды доступны менеджеру системы"""
        elif isinstance(user, Admin):
            message_text = help_text_admin + """

Выше приведённые команды доступны администратору системы"""
        self._message = message_text

    @Command.message.getter
    def message(self):
        return self._message

    @Command.key_word.getter
    def key_word(self):
        return "help"

    @Command.is_script.getter
    def is_script(self) -> bool:
        return False

    @Command.get_menu.getter
    def get_menu(self):
        return None
