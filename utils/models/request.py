import datetime
import string
import PIL.Image as Image
import io

from utils.models.user import User


class Request:
    __message: string
    __date: datetime
    __user: User
    __image: Image

    def __init__(self, message, date, user, image_bytes):
        self.__message = message
        self.__date = date
        self.__user = user
        self.__image = Image.open(io.BytesIO(image_bytes))
