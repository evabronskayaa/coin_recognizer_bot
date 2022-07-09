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
    x_list = list(set([user.get_start_date() for user in users]))
    y_list = []
    for x in x_list:
        count = 0
        for user in users:
            if user.get_start_date() == x:
                count += 1
        y_list.append(count)
    x_index = x_list
    x_labels = ['{0.month}.{0.day}.{0.year}'.format(x) for x in x_list]
    plt.xticks(x_index, x_labels)
    plt.bar(x_list, y_list, label="Новые пользователи")
    plt.legend()
    plt.savefig("../../chart.png", dpi=100)
    plt.close()
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
    x_index = x_list
    x_labels = ['{0.month}.{0.day}.{0.year}'.format(x) for x in x_list]
    plt.xticks(x_index, x_labels)
    plt.bar(x_list, y_list, label="Новые запросы", width=20)
    plt.legend()
    plt.savefig("../../assets/chart.png")
    plt.close()
    return InputFile("../../assets/chart.png")
