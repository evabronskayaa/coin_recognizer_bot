from datetime import datetime

from utils.db_models.models import UserDbModel, RequestDbModel
from utils.models.request import Request
from utils.models.user import User


def get_new_user(start_date=datetime.min, finish_date=datetime.today()):
    """get new user at intervals of time"""
    users = UserDbModel.select().where(start_date <= UserDbModel.start_date <= finish_date)
    return [User(user.name, user.id, user.start_date, user.money_account, user.is_manager, user.is_admin)
            for user in users]


def get_new_request(start_date=datetime.min, finish_date=datetime.today()):
    """get new request at intervals of time"""
    requests = RequestDbModel.select().where(start_date <= RequestDbModel.date <= finish_date)
    return [Request(request.id, request.message, request.date, User(t_id=request.user_id), request.rating,
                    request.image)
            for request in requests]