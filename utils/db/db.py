from utils.db_models.models import *


def init_db():
    db.create_tables([UserDbModel, ManagerDbModel, AdminDbModel, RequestDbModel, FollowDbModel])


init_db()
print(UserDbModel)
