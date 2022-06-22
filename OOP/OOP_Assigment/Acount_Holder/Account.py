class Accounta:

    def __init__(self, act, acno, bal):
        self.__account_number = acno
        self.__account_type = act
        self.balance = bal

    def get_account_number(self):
        return self.__account_number

    def set_account_number(self, __account_number):
        self.__account_number = __account_number

    def set_account_type(self, __account_type):
        self.__account_type = __account_type

    def get_account_type(self):
        return self.__account_type

    def set_balance(self, balance):
        self.balance = balance

    def get_balance(self):
        return self.balance

    def dipo(self, val):
        if val > 0:
            self.set_balance(self.get_balance()+val)
        else:
            pass

    def witro(self, val):
        if self.get_balance() > val:
            self.set_balance(self.get_balance()-val)
        else:
            print("in suffisiant bal")
