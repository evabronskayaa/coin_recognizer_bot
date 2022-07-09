import datetime
import string

from utils.models.user import User


class Request:
    _message: string
    _date: datetime
    _user: User
    _id: str
    _rating: bool

    def __init__(self, r_id, message, date, user, rating):
        self._message = message
        self._date = date
        self._user = user
        self._id = r_id
        self._rating = rating

    def to_string(self):
        return f'сообщение: {self._message}, дата: {self._date} '

    def get_id(self):
        return self._id

    def get_rating(self):
        return self._rating


class RequestData:
    first_date: datetime
    less_date: datetime
    user: User

    def __init__(self, first_date, less_date, user):
        self.first_date = first_date
        self.less_date = less_date
        self.user = user
