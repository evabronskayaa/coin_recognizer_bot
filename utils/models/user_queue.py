from utils.models.user import User


class UserQueue:
    _users = []
    _cur_user = User()

    def add_user(self, user):
        self._users.append(user)

    def pop_user(self):
        self._cur_user = self._users.pop()
        return self._cur_user

    def is_empty(self):
        return len(self._users) == 0

    def size(self):
        return len(self._users)

    def get_cur_user(self):
        return self._cur_user
