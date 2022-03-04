class Error(Exception):
    pass

class IdentityError(Error):
    pass

class OptionsError(Error):
    pass

class OperationError(Error):
    pass

class TaskError(Error):
    pass

class Users:
    Acc_No = 11111
    
    def __init__(self, name, mobile, address, balance):
        self.UserName = name
        self.Account_No = Users.Acc_No
        self.Mobile_No = mobile
        self.Adderss = address
        self.Account_Balance = balance
        Users.Acc_No += 1

class Manager:
    def __init__(self):   
        self.user_list = []
        
    def get_user_list(self):
        if len(self.user_list) == 0:
            print("No users found...!")
        else:
            for user in self.user_list:
                print('Account No.: {0}, Balance: {1}, User Name: {2}, Mobile No: {3}, Adrress: {4}'.format(user.Account_No,user.Account_Balance,user.UserName,user.Mobile_No,user.Adderss))

    def remove_user(self, acc_num):
        if len(self.user_list) == 0:
            print("There is no user to remove...!")
        else:
            for user in self.user_list:
                if user.Account_No == acc_num:
                    print("User with acc no. {} removed".format(acc_num))
                    self.user_list.remove(user)
                else:
                    print("Account does not exist")

class ATM:
    def get_user_details(user_list, acc_num):
        for user in user_list:
            if user.Account_No == acc_num:
                return user
        return False
        

manager_obj = Manager()

while True:
    try:
        identity = int(input("0: user \n1: manager \n2: quit \n"))
        if identity == 0:
            while True:
                try: 
                    options = int(input("0: enter existing account number \n1: add new account \n2: back\n"))
                    if options == 0:
                        acc_num = int(input("Enter account number: "))
                        account_exists = ATM.get_user_details(manager_obj.user_list, acc_num)
                        if account_exists:
                            while True:
                                try:
                                    atm_operation = int(input("\n0: display account details\n1: cash deposit\n2: cash withdrawal\n3: close account\n4: back\n"))
                                    if atm_operation == 0:
                                        print('Account No.: {0}\nAccount Balance: {1}\nName: {2}'.format(account_exists.Account_No, account_exists.Account_Balance, account_exists.UserName))
                                        
                                    elif atm_operation == 1:
                                        deposit_amount = int(input('Enter amount you want to deposit: '))
                                        account_exists.Account_Balance = int(account_exists.Account_Balance) + deposit_amount
                                        print("Balance after deposit; ", account_exists.Account_Balance)
                                        
                                    elif atm_operation == 2:
                                        withdrawal_amount = int(input('Enter amount you want to withdraw: '))
                                        if int(account_exists.Account_Balance) - withdrawal_amount >= 0:
                                            account_exists.Account_Balance = int(account_exists.Account_Balance) - withdrawal_amount - 0.5
                                            print("Balance after withdwawal; ", account_exists.Account_Balance)
                                        else:
                                            print("Insufficient Balance...!")
                                        
                                    elif atm_operation == 3:
                                        manager_obj.remove_user(acc_num)
                                        break

                                    elif atm_operation == 4:
                                        break
                                    else:
                                        raise OperationError
                                except OperationError:
                                    print("Enter 0, 1, 2, 3 or 4")
                                except ValueError:
                                    print("Enter numeric value")
                        else: 
                            print('Account does not exist')        
                    
                    elif options == 1:
                        user_name = input('Enter Your Name: ')
                        mobile_no = int(input('Enter Your mobile no.: '))
                        address = input('Enter Your adrress: ')
                        while True:
                            account_balance = int(input('Enter the deposit amount. Minimum balance limit: 10000. \n'))
                            if account_balance < 10000:
                                print("You need to add minimum 10000 Rs...")
                            else:
                                break
                        user = Users(user_name, mobile_no, address, account_balance)
                        manager_obj.user_list.append(user)
                        print('Account added...!\nYour Account no. is: {0}'.format(user.Account_No))

                    elif options == 2:
                        break
                    else:
                        raise OptionsError

                except OptionsError:
                    print("Enter 0, 1 or 2")
                except ValueError:
                    print("Enter numeric value")

        elif identity == 1:
            while True: 
                try:
                    task = int(input("0: view user list\n1: remove user\n2: back\n"))
                    if task == 0:
                        manager_obj.get_user_list()

                    elif task == 1:
                        manager_obj.remove_user(int(input("Enter Account number you want to remove: ")))

                    elif task == 2:
                        break
                    else:
                        raise TaskError
                except TaskError:
                    print("Enter 0, 1 or 2")
                except ValueError:
                     print("Enter numeric value")

        elif identity == 2:
            break

        else:
            raise IdentityError

    except IdentityError:
        print("Enter 0, 1 or 2")

    except ValueError:
        print("Enter numeric value")
