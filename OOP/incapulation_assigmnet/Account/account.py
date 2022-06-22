class Account:
    def __init__(self, name, account_no, account_type, __balance, __diposit, __withdrawal):
        self.name = name
        self.account_no = account_no
        self.account_type = account_type
        self.__diposit = __diposit
        self.__withdrawal = __withdrawal
        self.__balance = __balance

    def __str__(self):
        return "Name is={}\nAccount No.{}\nAccount Type={}".format(self.name, self.account_no, self.account_type)

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_account_no(self):
        return self.account_no

    def set_account_no(self, account_no):
        self.account_no = account_no

    def get_account_type(self):
        return self.account_type

    def set_account_type(self, account_type):
        self.account_type = account_type

    def get_balance(self):
        return self.__balance

    def dipo(self, val):
        if val > 0:
            balance = self.__balance+val
            print("Your Last Balance is {}\nNow creadit {}\n Total Balance is{}".format(
                self.__balance, val, balance))
        else:
            print("Please Enter Valid Amount")
        self.__balance = balance

    def withd(self, val):
        balance = self.__balance
        if val < self.__balance:
            balance = self.__balance-val
            print("Your Last Balance is {}\nNow Withdraw {}\n Total Balance is {}".format(
                self.__balance, val, balance))
