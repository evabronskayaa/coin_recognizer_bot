import os

from utils.db_models.models import *
from pathlib import *

def init_db():
    db.create_tables([UserDbModel, ManagerDbModel, AdminDbModel, RequestDbModel, FollowDbModel])


print(os.listdir())
#init_db()
