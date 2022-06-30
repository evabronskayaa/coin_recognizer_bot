from peewee import *

db = SqliteDatabase('')


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    name = TextField()
    user_id = CharField()


class Manager(BaseModel):
    name = TextField()
    user_id = CharField()


class Admin(BaseModel):
    name = TextField()
    user_id = CharField()


class Image(BaseModel):
    url = TextField()
    user_id = CharField()
    image_type = TextField()
    # + archive


class Favorites(BaseModel):
    url = TextField()
    user_id = CharField()


class History(BaseModel):
    url = TextField()
    user_id = CharField()