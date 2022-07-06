from utils.models.commands.command import Command


class StatCommand(Command):
    """Command for get statistics by manager"""

    def execute(self, user):
        pass

    @Command.message.getter
    def message(self):
        return "Выберте статистику которую хотите узнать"

    @Command.key_word.getter
    def key_word(self):
        return "stat"

    @Command.is_script.getter
    def is_script(self) -> bool:
        return False
