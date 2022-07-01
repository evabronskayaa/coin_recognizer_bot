from peewee import *

db = SqliteDatabase('')


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    name = CharField(null=False)
    id = IntegerField(unique=True, null=True, help_text="id that use in the Telegram", primary_key=True)
    start_date = DateTimeField(null=True)
    cash_account = IntegerField(null=True)


class Manager(BaseModel):
    token = CharField(null=True)
    user_id = ForeignKeyField(User, unique=True, null=True)


class Admin(BaseModel):
    user_id = ForeignKeyField(User, unique=True, null=True)


class Request(BaseModel):
    user_id = ForeignKeyField(User, unique=True, null=True)
    date = DateTimeField(null=True)
    message = CharField(null=False)
    data = BigBitField(null=True)
    id = IntegerField(unique=True, null=True, help_text="id of Request", primary_key=True)


class Follow(BaseModel):
    user_id = ForeignKeyField(User, unique=True, null=True)
    request_id = ForeignKeyField(Request, unique=True, null=True)
