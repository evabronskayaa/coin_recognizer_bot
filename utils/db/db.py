from utils.db_models.models import *


def init_db():
    db.create_tables([FollowDbModel])


init_db()
