from utils.models.commands.command import Command


class MoneySearch(Command):
    """Command for search money"""

    _continue = True

    def execute(self, data):
        self._continue = False
        # TODO search money

    @Command.message.getter
    def message(self):
        return 'отправляй фотографию'

    @Command.key_word.getter
    def key_word(self):
        return f"загрузить фото"

    @Command.is_script.getter
    def is_script(self) -> bool:
        return self._continue
