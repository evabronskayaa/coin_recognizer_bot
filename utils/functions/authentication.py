from utils.db_functions.user_functions import *


def authentication_with_start(context, t_user, chat_id):
    """
    Function for get current user
    :param chat_id:
    :param t_user: telegram user
    :param context: bot's context
    :return user: User | Admin
    """
    try:
        return authentication(context, t_user.id, chat_id)
    except:
        user = User(name=t_user.username, t_id=t_user.id, money=100)
        add_user(user)
        context.add_user(user)
        return user


def authentication(context, t_id, chat_id):
    """
    Function for get current user
    :param chat_id: telegram's chat id
    :param t_id: telegram id
    :param context: bot's context
    :return user: User | Admin
    """
    try:
        user = context.get_user_by_id(t_id)
        user.set_money(get_user_money(user))
        return user
    except:
        user = get_user_by_id(t_id)
        context.add_user(user, chat_id)
        return user
