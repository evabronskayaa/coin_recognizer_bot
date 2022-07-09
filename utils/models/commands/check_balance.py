from data.texts.balance_command_text import contact, error
from keyboards.inline.menu import *
from utils.models.commands.command import Command


class CheckBalance(Command):
    """Command for check money of user"""
    _message: str
    _continue = True
    _menu = None

    def execute(self, data):
        try:
            user = data
            name = user.get_name()
            money = user.get_money()
            self._message = f'{name}, Ваш баланс: {money} баллов'
            self._menu = get_balance_kb()
        except:
            if data.lower() == top_up.lower():
                self._message = contact
                self._menu = None
            else:
                self._message = error
            self._continue = False

    @Command.message.getter
    def message(self):
        return self._message

    @Command.key_word.getter
    def key_word(self):
        return 'баланс'

    @Command.is_script.getter
    def is_script(self) -> bool:
        return self._continue

    @Command.get_menu.getter
    def get_menu(self):
        return self._menu
