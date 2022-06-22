from new import FundException
from new import DipositException
from new import GenratecpassException
# try:
#     Balance = 5000
#     withdrawal = int(input("Enter Withdrawal Amount\n"))
#     count = withdrawal-Balance
#     if withdrawal > Balance:
#         raise FundException(count)
#     else:
#         remain = Balance-withdrawal
#         print("Collect Your Cash\nRemaining Balance is {}".format(remain))
# except FundException as e:
#     print(e)

# try:
#     diposit = int(input("Enter Diposit Amount=\n"))
#     total = remain+diposit
#     if diposit > 0:
#         print("Total Balance is= {}".format(total))
#     else:
#         raise DipositException(total)
# except DipositException as e:
#     print(e)

try:
    passw = input("Enter Your Password\n")
    if passw.isalnum() and passw.isdecimal() and passw.isspace() and passw.isalpha():
        print("Invalid Password!!\nPlease Choose 4 Digit Number")
        raise GenratecpassException()
    elif passw == 4:
        print("Your Password Genrate Succesfully Done")
except GenratecpassException as e:
    print(e)
