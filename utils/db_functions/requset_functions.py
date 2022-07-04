import datetime

from utils.db_models.models import *
from utils.models.request import Request
from utils.models.user import User


# function for get all request by user
def get_request(user: User, start_date: datetime = None):
    if start_date is None:
        requests_db = RequestDbModel.get(user_id=user.get_id())
    else:
        requests_db = RequestDbModel.select().where(RequestDbModel.date>=start_date).get(user_id = user.get_id())
    return [Request(message=request.message, date=request.date, user=user, image_bytes=request.data)
            for request in requests_db]


# function for add request in database
def add_request(user: User, message, data_bytes):
    _id = RequestDbModel.select(fn.Max(RequestDbModel.id)).scalar() + 1
    return RequestDbModel(date=datetime.date.today(), message=message, data=data_bytes, user_id=user.get_id()).save()
