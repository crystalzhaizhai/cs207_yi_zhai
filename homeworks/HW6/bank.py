from enum import Enum
class AccountType(Enum):
    SAVINGS = 1
    CHECKING = 2
    
class BankAccount():
    def __init__(self,owner,accountType):
        self.owner=owner
        self.accountType=accountType
        self.balance=0
    def withdraw(self,amount):
        if type(amount)!=int:
            raise ValueError("not integer amount")
        if amount<0:
            raise ValueError("amount<0")
        if self.balance<amount:
            raise ValueError("withdraw more than balance")
        self.balance-=amount
    def deposit(self,amount):
        if type(amount)!=int:
            raise ValueError("not integer amount")
        if amount<0:
            raise ValueError("amount<0")
        self.balance+=amount
    def __str__(self):
        return "owner:{!s} account type:{!s}".format(self.owner,self.accountType.name)
    def __len__(self):
        return self.balance
    
    
def ATMSession(bankUser):
    def Interface():
        option1=input("Enter Options:\
                        1)Exit\
                        2)Creat Account\
                        3)Check Balance\
                        4)Deposit\
                        5)Withdraw")
        if option1=="1":
            return
        option2=input("Enter Options:\
                        1)Checking\
                        2)Saving")
        if option1=="2":
            if option2=="1":
                bankUser.addAccount(AccountType.CHECKING)
                return
            elif option2=="2":
                bankUser.addAccount(AccountType.SAVINGS)
                return
            else:
                print("no such account type")
                raise AttributeError("no such account type")
        if option1=="3":
            if option2=="1":
                print(bankUser.getBalance(AccountType.CHECKING))
                return
            elif option2=="2":
                print(bankUser.getBalance(AccountType.SAVINGS))
                return
            else:
                print("no such account type")
                raise AttributeError("no such account type")
                
        if option1=="4":
            option3=input("Enter Interger Amount, Cannot be Negative:")
            if option2=="1":
                bankUser.deposit(AccountType.CHECKING,int(option3))
                return
            elif option2=="2":
                bankUser.deposit(AccountType.SAVINGS,int(option3))
                return
            else:
                print("no such account type")
                raise AttributeError("no such account type")
        
        if option1=="5":
            option3=input("Enter Interger Amount, Cannot be Negative:")
            if option2=="1":
                bankUser.withdraw(AccountType.CHECKING,int(option3))
                return
            elif option2=="2":
                bankUser.withdraw(AccountType.SAVINGS,int(option3))
                return
            else:
                print("no such account type")
                raise AttributeError("no such account type")
        print("no such operation")
        raise AttributeError("no such operation")
    return Interface