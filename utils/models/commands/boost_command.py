from utils.db_functions.user_functions import add_manager
from utils.models.commands.command import Command
from utils.models.user import User


class BoostCommand(Command):
    """Command for boost rules for admin"""

    _message = "Введите id пользователя кому вы хотите выдать права менеджера"
    _continue = True

    def execute(self, data):
        try:
            t_id = int(data)
            user = User(t_id=t_id)
            result = add_manager(user)
            if result is None:
                self._message = "Данный пользователь не найден"
            elif result:
                self._message = "Успешно"
            else:
                self._message = "Данный пользователь уже является Менеджером"
        except:
            self._message = "Это не id"
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
