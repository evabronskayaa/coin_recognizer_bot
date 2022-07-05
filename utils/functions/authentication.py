from utils.db_functions.user_functions import *


def authentication(context, t_id):
    try:
        return context.get_user_by_id(t_id)
    except:
        user = get_user_by_id(t_id)
        if check_on_admin(user):
            user = get_admin_by_user(user)
        context.add_user(user)
        return user
