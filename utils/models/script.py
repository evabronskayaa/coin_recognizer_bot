from utils.models.commands.command import Command
from utils.models.request import Request
from utils.models.user import User


class Script:
    _user: User
    _last_command: Command

    def __init__(self, user, command):
        self._user = user
        self._last_command = command

    def get_user(self):
        return self._user

    def set_user(self, user):
        if user is not None and user.get_id() >= 0:
            self._user = user
            return True
        return False

    def get_last_command(self):
        return self._last_command

    def set_last_command(self, command: Command):
        if command is not None:
            self._last_command = command
            return True
        return False

