from peewee import *

db = SqliteDatabase('')


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    name = CharField()
    id = PrimaryKeyField(unique=True)
    start_date = DateTimeField()
    cash_account = IntegerField()


class Manager(BaseModel):
    token = CharField()
    user_id = ForeignKeyField(User, unique=True)


class Admin(BaseModel):
    user_id = ForeignKeyField(User, unique=True)


class Request(BaseModel):
    user_id = ForeignKeyField(User, unique=True)
    date = DateTimeField()
    message = TextField()
    data = BigBitField()
    id = PrimaryKeyField(unique=True)


class Follow(BaseModel):
    user_id = ForeignKeyField(User, unique=True)
    request_id = ForeignKeyField(Request, unique=True)