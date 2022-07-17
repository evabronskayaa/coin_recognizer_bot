from utils.models.commands.command import Command


class OtherSearch(Command):
    """Command for search other objects"""

    _text = ''
    _continue = True

    async def execute(self, data):
        self._continue = False
        # TODO search object

    @Command.message.getter
    def message(self):
        return f'Жду фотографию'

    @Command.key_word.getter
    def key_word(self):
        return "Распознать по слову"

    @Command.is_script.getter
    def is_script(self) -> bool:
        return self._continue

    @Command.get_menu.getter
    def get_menu(self):
        return None

    # записываем то что будем искать на картинке
    def set_word(self, word):
        self._text = word
