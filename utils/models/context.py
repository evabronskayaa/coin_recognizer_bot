from utils.models.command import *
from utils.models.script import Script
from utils.models.user import User


class Context:
    _scripts = []

    def __init__(self):
        self._scripts: list[Script] = []

    def get_user_by_id(self, t_id):
        for user in [script.get_user() for script in self._scripts]:
            if user.get_id() == t_id:
                return user
        raise Exception('inccorect value')

    def add_user(self, user: User):
        users = [script.get_user() for script in self._scripts]
        if user.get_id() >= 0 or user.get_id() not in [user2.get_id() for user2 in users]:
            self._scripts.append(Script(user, None))

    def get_last_commdn(self, user: User) -> Command:
        for script in self._scripts:
            if script.get_user().get_id() is user.get_id():
                return script.get_last_command()
        raise Exception('script not found')
