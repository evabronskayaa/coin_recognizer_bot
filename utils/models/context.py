from utils.models.commands.command import Command
from utils.models.commands.nothing_command import NothingCommand
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
        raise Exception('incorrect value')

    def add_user(self, user: User, chat_id):
        users = [script.get_user() for script in self._scripts]
        if user.get_id() >= 0 or user.get_id() not in [user2.get_id() for user2 in users]:
            self._scripts.append(Script(user, NothingCommand(chat_id)))

    def _get_script(self, user):
        for script in self._scripts:
            if script.get_user().get_id() is user.get_id():
                return script
        raise Exception('script not found')

    def get_last_command(self, user: User) -> Command:
        try:
            return self._get_script(user).get_last_command()
        except:
            raise Exception('command not found')

    def set_last_command(self, user: User, command: Command) -> bool:
        try:
            self._get_script(user).set_last_command(command)
            return True
        except:
            return False

    def get_scripts(self):
        return self._scripts
