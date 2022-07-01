import datetime


class User:
    __name = ''
    __id = 0
    __start_date = datetime.date.today()
    __cash_account = 0

    def __init__(self, name='', t_id=0, date=datetime.date.today(), cash=0):
        self.name = name
        self.id = t_id
        self.__start_date = date
        self.__cash_account = cash


class Manager(User):
    __token = ''

    def __init__(self, name, t_id, date, cash, token):
        super().__init__(name, t_id, date, cash)
        self.__token = token


class Admin(User):

    def __init__(self, name, t_id, date, cash):
        super().__init__(name, t_id, date, cash)
