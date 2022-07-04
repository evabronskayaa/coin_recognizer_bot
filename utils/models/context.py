from aiogram.types import Message

from utils.models.user import User


class Context:
    _user: User

    def __init__(self, user=User()):
        self._user = user

    def get_user(self):
        return self._user

    def set_user(self, user: User):
        if user.get_id() >= 0:
            self._user = user
        else:
            raise Exception('incorrect user id')
