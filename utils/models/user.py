import datetime


class User:
    _name = ''
    _id = 0
    _start_date = datetime.date.today()
    _money_account = 0
    _is_manager = False
    _is_admin = False

    def __init__(self, name='', t_id=0, date=datetime.date.today(), money=0, manager=False, admin=False):
        self._name = name
        self._id = t_id
        self._start_date = date
        self._money_account = money
        self._is_manager = manager
        self._is_admin = admin

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_start_date(self):
        return self._start_date

    def get_money(self):
        return self._money_account

    def is_manager(self):
        return self._is_manager

    def is_admin(self):
        return self._is_admin
