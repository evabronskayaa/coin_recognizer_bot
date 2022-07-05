from utils.db_models.models import *
from utils.models.request import Request


def get_follows(user):
    """
    Function for get all follows of user
    :param user: User
    :return None:
    """
    follows = FollowDbModel.get(user_id=user.get_id())
    requests_db = [RequestDbModel.get(id=follow.request_id) for follow in follows]
    return [Request(message=request.message, date=request.date, user=user, image_bytes=request.data)
            for request in requests_db]


def add_follow(request_id, user):
    """
    Function for add follow in database
    :param request_id: int
    :param user: User
    :return None:
    """
    FollowDbModel(request_id=request_id, user_id=user.get_id()).save()
