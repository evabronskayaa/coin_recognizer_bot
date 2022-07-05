from utils.models.user import User


class Context:
    _users = []

    def __init__(self):
        self._users: list[User] = []

    def get_user_by_id(self, t_id):
        for user in self._users:
            if user.get_id() == t_id:
                return user
        raise Exception('inccorect value')

    def add_user(self, user: User):
        if user.get_id() >= 0 | user.get_id() not in [user2.get_id() for user2 in self._users]:
            self._users.append(user)
        else:
            raise Exception('incorrect user id')
