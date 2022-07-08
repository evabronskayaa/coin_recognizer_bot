from datetime import datetime

from utils.db_models.models import *
from utils.models.request import Request
from utils.models.user import User


def get_requests(user: User, start_date=datetime.min, finish_date=datetime.today()):
    """
    Function for get all request of user
    :param finish_date: datetime, optional parameter
    :param start_date: datetime, optional parameter
    :param user: User
    :return requests: list[Request]
    """
    requests_db = RequestDbModel.select()\
        .where(finish_date >= RequestDbModel.date >= start_date & RequestDbModel.user_id == user.get_id())
    return [Request(message=request.message, date=request.date, user=user, rating=request.rating, r_id=request.id)
            for request in requests_db]


def add_request(user: User, message, r_id, rating):
    """
    Function for add request in database
    :param rating: photo's rating
    :param r_id: telegram id of photo
    :param message: text
    :param user: User
    :return None:
    """
    try:
        RequestDbModel.create(date=datetime.date.today(), message=message,
                              id=r_id, user_id=user.get_id(), rating=rating)
        return True
    except:
        return False
