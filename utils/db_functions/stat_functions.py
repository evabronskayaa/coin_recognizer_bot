import datetime

from utils.db_models.models import UserDbModel, RequestDbModel
from utils.models.request import Request
from utils.models.user import User


def get_new_user(start_date=datetime.MINYEAR, finish_date=datetime.date.today()):
    """get new user at intervals of time"""
    users = UserDbModel.select().where(start_date <= UserDbModel.start_date <= finish_date)
    return [User(user.name, user.id, user.start_date, user.money_account)
            for user in users]


def get_new_request(start_date=datetime.MINYEAR, finish_date=datetime.date.today()):
    """get new request at intervals of time"""
    requests = RequestDbModel.select().where(start_date <= RequestDbModel.date <= finish_date)
    return [Request(request.message, request.message, request.data, User(t_id=request.user_id))
            for request in requests]
