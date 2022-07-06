from utils.db_models.models import *
from utils.models.user import *


# function for get user by id from Data Base
def get_user_by_id(t_id):
    """
    get user from table
    :param t_id: id of telegram user
    :return User:
    """
    user = UserDbModel.get(id=t_id)
    return User(name=user.name, t_id=user.id, date=user.start_date, money=user.money_account)


def add_user(user: User):
    """
    add user in table
    :param user:
    :return None:
    """
    UserDbModel.create(name=user.get_name(), id=user.get_id(), start_date=user.get_start_date(),
                       money_account=user.get_money())


def check_on_admin(user: User):
    """
    function for check admin rules:
    :param user: User
    :return boolean:
    """
    try:
        AdminDbModel.get_by_id(user.get_id())
    except Exception:
        return False
    finally:
        return True


def get_admin_by_id(t_id):
    """
    Function for get admin user
    :param t_id:
    :return Admin:
    """
    admin = AdminDbModel.get(user_id=t_id)
    user = get_user_by_id(admin.user_id)
    return Admin(user=user)


def get_admin_by_user(user):
    """
    Function for get admin user
    :param user: User
    :return Admin:
    """
    return Admin(user=user)


def check_on_manager(user: User):
    """
    Function for check manager rules
    :param user: User
    :return bool:
    """
    try:
        ManagerDbModel.get_by_id(user.get_id())
    except Exception:
        return False
    finally:
        return True


def get_manager_by_id(t_id):
    """
    Function for get manager rules
    :param t_id: int
    :return Manager:
    """
    manager = ManagerDbModel.get(user_id=t_id)
    user = get_user_by_id(manager.user_id)
    return Manager(user=user, token="")


def get_manager_by_user(user):
    """
    Function for get admin user
    :param user: User
    :return Manager:
    """
    return Manager(user=user, token="")


def add_manager(user):
    """
    Function for add manager in table
    :param user: User
    :return: bool | None
    """
    try:
        ManagerDbModel.get(user_id=user.get_id())
        return False
    except:
        try:
            UserDbModel.get(id=user.get_id())
            ManagerDbModel.create(user_id=user.get_id())
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
        manager = ManagerDbModel.get(user_id=user.get_id())
        manager.delete_instance()
        return True
    except:
        return False
