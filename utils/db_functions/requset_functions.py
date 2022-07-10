import datetime

from utils.db_models.models import *
from utils.models.request import Request
from utils.models.user import User


def get_requests(user: User, start_date=datetime.MINYEAR, finish_date=datetime.date.today()):
    """
    Function for get all request of user
    :param finish_date: datetime, optional parameter
    :param start_date: datetime, optional parameter
    :param user: User
    :return requests: list[Request]
    """
    requests_db = RequestDbModel.select()\
        .where((finish_date >= RequestDbModel.date >= start_date)
               & (RequestDbModel.user_id == user.get_id()))
    return [Request(message=request.message, date=request.date, user=user, rating=request.rating, r_id=request.id,
                    data=request.image)
            for request in requests_db]


def add_request(r_id, user: User, message, image_data, date=datetime.date.today(), rating=None):
    """
    Function for add request in database
    :param date:
    :param image_data:
    :param rating: photo's rating
    :param r_id: telegram id of photo
    :param message: text
    :param user: User
    :return None:
    """
    if rating is None:
        RequestDbModel.create(date=date, message=message,
                              id=r_id, user_id=user.get_id(), image=image_data)
    else:
        RequestDbModel.create(date=date, message=message,
                              id=r_id, user_id=user.get_id(), image=image_data, rating=rating)

