from utils.db_models.models import *
from utils.models.follow import Follow
from utils.models.user import User


def get_follows(user: User):
    """
    Function for get all follows of user
    :param user: User
    :return None:
    """
    follows = FollowDbModel.select().where(FollowDbModel.user_id == user.get_id())
    return [Follow(follow.request_id, user) for follow in follows]


def add_follow(request, user):
    """
    Function for add follow in database
    :param request: Request
    :param user: User
    :return None:
    """
    FollowDbModel.create(request_id=request, user_id=user.get_id())
