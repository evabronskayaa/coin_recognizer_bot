from peewee import *

db = SqliteDatabase("utils/db/database.db")


class BaseModel(Model):
    class Meta:
        database = db


class UserDbModel(BaseModel):
    name = CharField(null=True)
    id = IntegerField(unique=True, null=False, help_text="id that use in the Telegram", primary_key=True)
    start_date = DateTimeField(null=False, help_text="start date of using the bot")
    cash_account = IntegerField(null=False)

    class Meta:
        order_by = 'start_date'
        db_table = 'Users'


class Worker(BaseModel):
    user_id = ForeignKeyField(UserDbModel, unique=True, null=False)


class ManagerDbModel(Worker):
    token = CharField(null=False, primary_key=True)

    class Meta:
        db_table = 'Managers'


class AdminDbModel(Worker):
    class Meta:
        db_table = 'Admins'


class RequestDbModel(Worker):
    date = DateTimeField(null=False)
    message = CharField(null=True)
    data = BigBitField(null=False)
    id = IntegerField(unique=True, null=False, help_text="id of Request", primary_key=True)

    class Meta:
        order_by = 'date'
        db_table = 'Requests'


class FollowDbModel(Worker):
    request_id = ForeignKeyField(RequestDbModel, unique=True, null=False, primary_key=True)

    class Meta:
        db_table = 'Follows'
