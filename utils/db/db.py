from utils.db_models.db_models import *


def init_db():
    db.create_tables([User, Manager, Admin, Request, Follow])


init_db()
print(User)
