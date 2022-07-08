import datetime
import string
import PIL.Image as Image
import io

from utils.models.user import User


class Request:
    _message: string
    _date: datetime
    _user: User
    _image_bytes = []

    def __init__(self, message, date, user, image_bytes):
        self._message = message
        self._date = date
        self._user = user
        if image_bytes is not None:
            self._image_bytes = image_bytes

    def to_string(self):
        return f"сообщение: {self._message}, дата: {self._date} "

    def get_image_bytes(self):
        return self._image_bytes


class RequestData:
    first_date: datetime
    less_date: datetime
    user: User

    def __init__(self, first_date, less_date, user):
        self.first_date = first_date
        self.less_date = less_date
        self.user = user
