from utils.models.commands.command import Command


class CheckBalance(Command):
    """Command for check money of user"""
    _message: str

    def execute(self, data):
        try:
            user = data
            name = user.get_name()
            money = user.get_money()
            self._message = f"{name}, ваш баланс: {money} баллов"
        except:
            self._message = "Техническая ошибка"

    @Command.message.getter
    def message(self):
        return self._message

    @Command.key_word.getter
    def key_word(self):
        return "баланс"

    @Command.is_script.getter
    def is_script(self) -> bool:
        return False
