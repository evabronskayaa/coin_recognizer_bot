import datetime
import string

from utils.models.user import User


class Request:
    _message: string
    _date: datetime
    _user: User
    _id: str
    _rating: bool
    _data: list

    def __init__(self, r_id, message, date, user, rating, data):
        self._message = message
        self._date = date
        self._user = user
        self._id = r_id
        self._rating = rating
        self._data = data

    def to_string(self):
        return f'сообщение: {self._message}, дата: {self._date} '

    def get_id(self):
        return self._id

    def get_rating(self):
        return self._rating

    def get_date(self):
        return self._date

    def get_images_bytes(self):
        return self._data

    def get_message(self):
        return self._message
