from utils.models.user import User


class Context:
    __user: User

    def __init__(self, user=User()):
        __user = user

    def get_user(self):
        return self.__user

    def set_user(self, user: User):
        if user.get_id() >= 0:
            self.__user = user
        else:
            raise Exception('incorrect user id')
