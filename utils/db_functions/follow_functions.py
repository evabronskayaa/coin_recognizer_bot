from utils.db_models.models import *
from utils.models.request import Request


# function for get all follows of user
def get_follows(user):
    follows = FollowDbModel.get(user_id=user.get_id())
    requests_db = [RequestDbModel.get(id=follow.request_id) for follow in follows]
    return [Request(message=request.message, date=request.date, user=user, image_bytes=request.data)
            for request in requests_db]


# function for add follow in database
def add_follow(request_id, user):
    FollowDbModel(request_id=request_id, user_id=user.get_id()).save()
