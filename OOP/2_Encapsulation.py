# ------------- Encapsulation --------------
class Bank: 
    def __init__(self):
        self.__balance = 1000    # Private Attribute 
    
    def showBalance(self):
        print(self.__balance)
    
b = Bank()
b.showBalance()