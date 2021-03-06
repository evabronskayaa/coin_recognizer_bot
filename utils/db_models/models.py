from peewee import *

db = SqliteDatabase("utils/db/database.db")


class BaseModel(Model):
    class Meta:
        database = db


class UserDbModel(BaseModel):
    name = CharField(null=True)
    id = IntegerField(unique=True, null=False, help_text="id that use in the Telegram", primary_key=True)
    start_date = DateTimeField(null=False, help_text="start date of using the bot")
    money_account = IntegerField(null=False)
    is_manager = BooleanField(null=False)
    is_admin = BooleanField(null=False)

    class Meta:
        order_by = 'start_date'
        db_table = 'Users'


class Worker(BaseModel):
    user_id = ForeignKeyField(UserDbModel, unique=False, null=False)


class RequestDbModel(Worker):
    date = DateTimeField(null=False)
    message = CharField(null=True)
    rating = BooleanField(null=True)
    id = CharField(null=False, help_text="telegram id of Request", primary_key=True)
    image = BlobField(null=False)

    class Meta:
        order_by = 'date'
        db_table = 'Requests'


class FollowDbModel(Worker):
    request_id = ForeignKeyField(RequestDbModel, primary_key=True)

    class Meta:
        db_table = 'Follows'
