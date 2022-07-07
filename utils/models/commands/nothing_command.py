from utils.models.commands.command import Command


class NothingCommand(Command):
    """Command that does nothing"""

    def execute(self, data):
        pass

    @Command.message.getter
    def message(self):
        return 'Моя твоя не понимать'

    @Command.key_word.getter
    def key_word(self):
        return ""

    @Command.is_script.getter
    def is_script(self) -> bool:
        return False

    @Command.get_menu.getter
    def get_menu(self):
        return None
