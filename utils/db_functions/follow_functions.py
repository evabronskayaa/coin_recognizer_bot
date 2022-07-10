from utils.db_models.models import *
from utils.models.follow import Follow
from utils.models.request import Request
from utils.models.user import User


def get_follows(user: User):
    """
    Function for get all follows of user
    :param user: User
    :return None:
    """
    follows = [Follow(follow.user_id, follow.request_id) for follow in
               FollowDbModel.select().where(FollowDbModel.user_id == user.get_id())]
    requests_db = []
    for follow in follows:
        for req in RequestDbModel.select().where(RequestDbModel.id == follow.r_id):
            requests_db.append(req)

    return [Request(message=request.message, date=request.date, user=user, r_id=request.id, rating=request.rating,
                    data=request.image)
            for request in requests_db]


def add_follow(request, user):
    """
    Function for add follow in database
    :param request: Request
    :param user: User
    :return None:
    """
    FollowDbModel.create(request_id=request, user_id=user.get_id())
