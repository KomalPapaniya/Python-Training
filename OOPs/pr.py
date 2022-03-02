class Users:
    def __init__(self, name, acc_no, mob_no, address, balance):
        self.UserName = name
        self.Account_No = acc_no
        self.Mobile_No = mob_no
        self.Adderss = address
        self.Account_Balance = balance

c = Users('komal', 123, 456, 'abc', 1000)
print(c.Account_No)