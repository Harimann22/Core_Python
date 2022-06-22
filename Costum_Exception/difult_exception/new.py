class FundException(Exception):
    def __init__(self, count):
        super().__init__("Insuficiant Balance-{} Rs. Less". format(count))


class DipositException(Exception):
    def __init__(self, total):
        super().__init__("Enter a Valid Amount")


class GenratecpassException(Exception):
    def __init__(self):
        super().__init__("Invalid Password!!\nPlease Choose 4 Digit Number")
