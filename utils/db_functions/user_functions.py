from utils.db_models.models import *
from utils.models.user import *


# function for get user by id from Data Base
def get_user_by_id(t_id):
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
    """function for check admin rules: """
    try:
        AdminDbModel.get_by_id(user.get_id())
    except Exception:
        return False
    finally:
        return True


def get_admin_by_id(t_id):
    """function for get admin user"""
    admin = AdminDbModel.get(user_id=t_id)
    user = get_user_by_id(admin.user_id)
    return Admin(user=user)


def get_admin_by_user(user):
    """function for get admin user"""
    return Admin(user=user)


def check_on_manager(user: User):
    """function for check manager rules"""
    try:
        ManagerDbModel.get_by_id(user.get_id())
    except Exception:
        return False
    finally:
        return True


def get_manager_by_id(t_id):
    """function for get manager rules"""
    manager = ManagerDbModel.get(user_id=t_id)
    user = get_user_by_id(manager.user_id)
    return Manager(user=user, token="")


def get_manager_by_user(user):
    """function for get admin user"""
    return Manager(user=user, token="")
