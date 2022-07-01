from peewee import *
from data.config import DB_PATH
db = SqliteDatabase(DB_PATH)


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    name = CharField(null=True)
    id = IntegerField(unique=True, null=False, help_text="id that use in the Telegram", primary_key=True)
    start_date = DateTimeField(null=False, help_text="start date of using the bot")
    cash_account = IntegerField(null=False)

    class Meta:
        order_by = 'start_date'
        db_table = 'Users'


class Worker(BaseModel):
    user_id = ForeignKeyField(User, unique=True, null=False)


class Manager(Worker):
    token = CharField(null=False, primary_key=True)

    class Meta:
        db_table = 'Managers'


class Admin(Worker):

    class Meta:
        db_table = 'Admins'


class Request(Worker):
    date = DateTimeField(null=False)
    message = CharField(null=True)
    data = BigBitField(null=False)
    id = IntegerField(unique=True, null=False, help_text="id of Request", primary_key=True)

    class Meta:
        order_by = 'date'
        db_table = 'Requests'


class Follow(Worker):
    request_id = ForeignKeyField(Request, unique=True, null=False, primary_key=True)

    class Meta:
        db_table = 'Follows'
