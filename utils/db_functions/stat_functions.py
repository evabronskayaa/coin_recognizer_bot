from utils.db_models.models import UserDbModel, RequestDbModel


def get_new_user(start_date, finish_date):
    """get new user at intervals of time"""
    return UserDbModel.select().where(start_date <= UserDbModel.start_date <= finish_date).get()


def get_new_request(start_date, finish_date):
    """get new request at intervals of time"""
    return RequestDbModel.select().where(start_date <= RequestDbModel.date <= finish_date).get()
