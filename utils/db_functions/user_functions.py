from utils.db_models.models import *
from utils.models.user import *


def get_user_by_id(t_id):
    """
    function for get user by id from Data Base
    :param t_id: id of telegram user
    :return User:
    """
    user = UserDbModel.get(UserDbModel.id == t_id)
    return User(name=user.name, t_id=user.id, date=user.start_date, money=user.money_account,
                manager=user.is_manager, admin=user.is_admin)


def get_user_by_name(name):
    """
    function for get user by name from Data Base
    :param name: username
    :return User:
    """
    user = UserDbModel.get(UserDbModel.name == name)
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


def add_manager_by_id(t_id):
    """
    Function for add manager in table by id
    :param t_id: telegram id of user
    :return: bool | None
    """
    try:
        user = UserDbModel.get(UserDbModel.id == t_id)
        if user.is_manager:
            return False
        else:
            user.is_manager = True
            user.save()
            return True
    except:
        return None


def add_manager_by_name(name):
    """
    Function for add manager in table by name
    :param name: user's username
    :return: bool | None
    """
    try:
        user = UserDbModel.get(UserDbModel.name == name)
        if user.is_manager:
            return False
        else:
            user.is_manager = True
            user.save()
            return True
    except:
        return None


def remove_manager_by_id(t_id):
    """
    Function for remove manager from table
    :param t_id: telegram id
    :return:bool
    """
    try:
        user = UserDbModel.get(UserDbModel.id == t_id)
        if user.is_manager:
            user.is_manager = False
            user.save()
            return True
        else:
            return False
    except:
        return None


def remove_manager_by_name(name):
    """
    Function for remove manager from table
    :param name: username
    :return:bool
    """
    try:
        user = UserDbModel.get(UserDbModel.name == name)
        if user.is_manager:
            user.is_manager = False
            user.save()
            return True
        else:
            return False
    except:
        return None


def update_user(user: User):
    UserDbModel(id=user.get_id(), name=user.get_name(), start_date=user.get_start_date(),
                money_account=user.get_money(), is_manager=user.is_manager(), is_admin=user.is_admin()).save()


def get_user_money(user: User):
    return get_user_by_id(user.get_id()).get_money()
