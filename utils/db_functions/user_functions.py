from utils.db_models.models import *
from utils.models.user import *


# function for get user by id from Data Base
def get_user_by_id(t_id):
    user = UserDbModel.get(id=t_id)
    return User(name=user.name, t_id=user.id, date=user.start_date, cash=user.cash_account)


# add user in table
def add_user(user: User):
    UserDbModel.create(name=user.get_name(), id=user.get_id(), start_date=user.get_start_date(),
                       cash_account=user.get_cash()).save()


# function for check admin rules
def check_on_admin(user: User):
    try:
        AdminDbModel.get_by_id(user.get_id())
    except Exception:
        return False
    finally:
        return True


# function for get admin user
def get_admin(user: User):
    admin = AdminDbModel.get(user_id=user.get_id())
    return Admin(user=user)


# function for check manager rules
def check_on_manager(user: User):
    try:
        ManagerDbModel.get_by_id(user.get_id())
    except Exception:
        return False
    finally:
        return True
