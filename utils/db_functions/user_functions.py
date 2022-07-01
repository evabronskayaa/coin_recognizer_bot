from utils.db_models.models import *
from utils.models.user import *

def get_user_by_id(t_id):
    user = User.get_by_id(t_id)
    return User(name=user.name,)