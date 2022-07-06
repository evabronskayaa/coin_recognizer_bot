from utils.db_functions.requset_functions import get_request
from utils.models.commands.command import Command
from utils.models.user import User


class HistoryCommand(Command):
    """Command for get history of command"""
    _message: str
    _user: User
    _continue = False

    def execute(self, data):
        if isinstance(data, User) and not self._continue:
            self._user = data
            self._continue = True
            self._message = "выберите дату"
        elif data.lower() == "посмотреть полностью" and self._continue:
            try:
                user = self._user
                for request in get_request(user):
                    self._message += request.to_string() + "\n"
            except:
                self._message = "вы еще не делали запросы"
            self._continue = False
        else:
            self._message = "Неправельные данные"
            self._continue = False

    @Command.message.getter
    def message(self):
        return self._message

    @Command.key_word.getter
    def key_word(self):
        return "история"

    @Command.is_script.getter
    def is_script(self) -> bool:
        return self._continue
