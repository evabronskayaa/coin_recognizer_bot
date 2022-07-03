import datetime


class User:
    __name = ''
    __id = 0
    __start_date = datetime.date.today()
    __money_account = 0

    def __init__(self, name='', t_id=0, date=datetime.date.today(), money=0):
        self.__name = name
        self.__id = t_id
        self.__start_date = date
        self.__money_account = money

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_start_date(self):
        return self.__start_date

    def get_money(self):
        return self.__money_account


class Manager(User):
    __token = ''

    def __init__(self, user, token):
        super().__init__(user.get_name(), user.get_id(), user.get_start_date(), user.get_money())
        self.__token = token


class Admin(User):

    def __init__(self, user):
        super().__init__(user.get_name(), user.get_id(), user.get_start_date(), user.get_money())
