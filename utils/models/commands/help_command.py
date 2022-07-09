from data.texts.help_command_text import *
from utils.models.commands.command import Command


class HelpCommand(Command):
    """Command for get help message"""

    _message = " "

    def execute(self, user):
        message_text = help_text
        if user.is_manager():
            message_text = help_text_manager + """

Выше приведённые команды доступны менеджеру системы"""
        elif user.is_admin():
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
