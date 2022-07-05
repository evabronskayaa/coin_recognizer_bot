from utils.db_functions.user_functions import *


def authentication(context, t_user):
    """
    Function for get current user
    :param t_user: telegram user
    :param context: bot's context
    :return user: User | Admin
    """
    try:
        return context.get_user_by_id(t_user.id)
    except:
        try:
            user = get_user_by_id(t_user.id)
            if check_on_admin(user):
                user = get_admin_by_user(user)
            context.add_user(user)
            return user
        except:
            user = User(name=t_user.first_name, t_id=t_user.id, money=100)
            add_user(user)
            context.add_user(user)
            return user
