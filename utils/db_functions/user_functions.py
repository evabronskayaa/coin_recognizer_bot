from utils.db_models.models import *
from utils.models.user import *


# function for get user by id from Data Base
def get_user_by_id(t_id):
    user = UserDbModel.get(id=t_id)
    return User(name=user.name, t_id=user.id, date=user.start_date, money=user.money_account)


# add user in table
def add_user(user: User):
    UserDbModel.create(name=user.get_name(), id=user.get_id(), start_date=user.get_start_date(),
                       cash_account=user.get_money()).save()


# function for check admin rules
def check_on_admin(user: User):
    try:
        AdminDbModel.get_by_id(user.get_id())
    except Exception:
        return False
    finally:
        return True


# function for get admin user
def get_admin_by_id(t_id):
    admin = AdminDbModel.get(user_id=t_id)
    user = get_user_by_id(admin.user_id)
    return Admin(user=user)


# function for get admin user
def get_admin_by_user(user):
    return Admin(user=user)


# function for check manager rules
def check_on_manager(user: User):
    try:
        ManagerDbModel.get_by_id(user.get_id())
    except Exception:
        return False
    finally:
        return True


# function for get manager rules
def get_manager_by_id(t_id):
    manager = ManagerDbModel.get(user_id=t_id)
    user = get_user_by_id(manager.user_id)
    return Manager(user=user, token="")


# function for get admin user
def get_manager_by_user(user):
    return Manager(user=user, token="")
