from utils.db_models.models import *


def init_db():
    db.create_tables([UserDbModel])


init_db()
