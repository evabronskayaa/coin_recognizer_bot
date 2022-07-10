from utils.models.user import User


class Follow:
    _r_id: str
    _user: User

    def __int__(self, r_id, user):
        self._r_id = r_id
        self._user = user

    def get_request_id(self):
        return self._r_id

    def get_user(self):
        return self._user
