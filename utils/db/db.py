from peewee import *


db = SqliteDatabase('')


class BaseModel(Model):
    class Meta:
        database = db


def init_db():
    db.create_tables()