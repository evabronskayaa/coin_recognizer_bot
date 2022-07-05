from utils.models.command import *
from utils.models.user import User


class Context:
    _users = []
    _last_command: Command

    def __init__(self):
        self._users: list[User] = []
        self._last_command = NothingCommand()

    def get_user_by_id(self, t_id):
        for user in self._users:
            if user.get_id() == t_id:
                return user
        raise Exception('inccorect value')

    def add_user(self, user: User):
        if user.get_id() >= 0 | user.get_id() not in [user2.get_id() for user2 in self._users]:
            self._users.append(user)

    def get_last_command(self):
        return self._last_command

    def set_last_command(self, command):
        if not isinstance(command, NothingCommand):
            self._last_command = command
