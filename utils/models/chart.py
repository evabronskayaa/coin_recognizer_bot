import matplotlib.pyplot as plt
from aiogram.types import InputFile

from utils.models.Type import Type
from utils.models.request import Request
from utils.models.user import User


def build_chart(stat, s_type):
    if s_type == Type.USER:
        return _build_chart_user(stat)
    elif s_type == Type.REQUEST:
        return _buils_chart_request(stat)
    else:
        raise Exception('incorrect type of stat')


def _build_chart_user(users: list[User]):
    x_list = [user.get_start_date() for user in users]
    y_list = []
    for x in x_list:
        count = 0
        for user in users:
            if user.get_start_date() == x:
                count += 1
        y_list.append(count)
    plt.plot(x_list, y_list)
    plt.savefig("../../chart.png", dpi=100)
    return InputFile("../../chart.png")


def _buils_chart_request(requests: list[Request]):
    x_list = [request.get_date() for request in requests]
    y_list = []
    for x in x_list:
        count = 0
        for request in requests:
            if request.get_date() == x:
                count += 1
        y_list.append(count)
    plt.plot(x_list, y_list)
    plt.savefig("../../assets/chart.png")
    return InputFile("../../assets/chart.png")
