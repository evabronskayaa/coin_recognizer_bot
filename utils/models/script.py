from utils.models.command import Command, NothingCommand
from utils.models.user import User


class Script:
    _user: User
    _last_coomand: Command

    def __init__(self, user, command):
        self._user = user
        self._last_coomand = command

    def get_user(self):
        return self._user

    def set_user(self, user):
        if user is not None and user.get_id() >= 0:
            self._user = user
            return True
        return False

    def get_last_command(self):
        return self._last_coomand

    def set_last_command(self, command: Command):
        if command is not None:
            self._last_coomand = command
            return True
        return False

