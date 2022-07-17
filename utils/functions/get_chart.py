from datetime import timedelta

import matplotlib.pyplot as plt
import seaborn as sns
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
    sns.set_theme(style="darkgrid")
    sns.barplot(x=x_list, y=y_list, label="Новые пользователи")
    plt.legend()
    plt.savefig("../../chart.png", dpi=100)
    plt.close()
    return InputFile("../../chart.png")


def _buils_chart_request(requests: list[Request]):
    width = 0.5
    x_list = list(set([request.get_date() for request in requests]))
    indexs = range(0, len(x_list))
    simple = get_simple_chart(x_list, requests)
    good = get_good_chart(x_list, requests)
    bad = get_bad_chart(x_list, requests)
    x_labels = ['{0.day}.{0.month}.{0.year}'.format(x) for x in x_list]

    sns.set_theme(style="darkgrid")
    plt.xticks(indexs, x_labels)
    plt.bar(indexs, simple, label="Новые запросы", width=width/2)
    plt.legend()
    plt.bar([value+width*0.65 for value in indexs], good, label="Положительные запросы", width=width/2)
    plt.legend()
    plt.bar([value+width*1.3 for value in indexs], bad, label="Негативные запросы", width=width/2)
    plt.legend()
    plt.savefig("../../chart.png")
    plt.close()
    return InputFile("../../chart.png")


def get_simple_chart(x_list, requests):
    y_list = []
    for x in x_list:
        count = 0
        for request in requests:
            if request.get_date() == x:
                count += 1
        y_list.append(count)
    return y_list


def get_good_chart(x_list, requests):
    y_list = []
    for x in x_list:
        count = 0
        for request in requests:
            rating = request.get_rating()
            if request.get_date() == x and rating is not None and rating is True:
                count += 1
        y_list.append(count)
    return y_list


def get_bad_chart(x_list, requests):
    y_list = []
    for x in x_list:
        count = 0
        for request in requests:
            rating = request.get_rating()
            if request.get_date() == x and rating is not None and rating is False:
                count += 1
        y_list.append(count)
    return y_list
