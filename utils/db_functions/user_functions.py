from utils.db_models.models import *
from utils.models.user import *


# function for get user by id from Data Base
def get_user_by_id(t_id):
    """
    get user from table
    :param t_id: id of telegram user
    :return User:
    """
    user = UserDbModel.get(UserDbModel.id == t_id)
    return User(name=user.name, t_id=user.id, date=user.start_date, money=user.money_account,
                manager=user.is_manager, admin=user.is_admin)


def add_user(user: User):
    """
    add user in table
    :param user:
    :return None:
    """
    UserDbModel.create(name=user.get_name(), id=user.get_id(), start_date=user.get_start_date(),
                       money_account=user.get_money(), is_manager=user.is_manager(), is_admin=user.is_admin())


def add_manager(user):
    """
    Function for add manager in table
    :param user: User
    :return: bool | None
    """
    try:
        UserDbModel.get(UserDbModel.id == user.get_id() & UserDbModel.is_manager == False)
        return False
    except:
        try:
            add_user(user)
            return True
        except:
            return None


def remove_manager(user):
    """
    Function for remove manager from table
    :param user:
    :return:bool
    """
    try:
        manager = UserDbModel.get(UserDbModel.id == user.get_id() & UserDbModel.is_manager == True)
        manager.is_manager = False
        manager.save()
        return True
    except:
        try:
            UserDbModel.get(UserDbModel.id == user.get_id())
            return False
        except:
            return None
