from utils.db_models.models import *
from utils.models.user import *

def get_follows(t_id):
    follows = FollowDbModel.select().where(user_id=t_id)