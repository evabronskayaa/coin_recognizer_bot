from utils.db_models.models import *
from utils.models.user import *


# function for get user by id from Data Base
def get_user_by_id(t_id):
    user = UserDbModel.get_by_id(t_id)
    return User(name=user.name, t_id=user.id, date=user.start_date, cash=user.cash_account)


# function for check admin rules
def check_on_admin(user: User):
    try:
        AdminDbModel.get_by_id(user.get_id())
    except Exception:
        return False
    finally:
        return True


# function for check manager rules
def check_on_manager(user: User):
    try:
        ManagerDbModel.get_by_id(user.get_id())
    except Exception:
        return False
    finally:
        return True
