import datetime

from utils.db_models.models import *
from utils.models.request import Request
from utils.models.user import User


def get_request(user: User, start_date: datetime = None):
    """
    Function for get all request of user
    :param start_date: datetime, optional parameter
    :param user: User
    :return requests: list[Request]
    """
    if start_date is None:
        requests_db = RequestDbModel.get(user_id=user.get_id())
    else:
        requests_db = RequestDbModel.select().where(RequestDbModel.date>=start_date).get(user_id = user.get_id())
    return [Request(message=request.message, date=request.date, user=user, image_bytes=request.data)
            for request in requests_db]


def add_request(user: User, message, data_bytes):
    """
    Function for add request in database
    :param data_bytes: bytes of image
    :param message: text
    :param user: User
    :return None:
    """
    _id = RequestDbModel.select(fn.Max(RequestDbModel.id)).scalar() + 1
    return RequestDbModel(date=datetime.date.today(), message=message, data=data_bytes, user_id=user.get_id()).save()
