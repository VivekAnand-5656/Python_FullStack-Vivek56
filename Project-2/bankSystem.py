# # =========================== Mini Bank Management System =================

# class BankAccount:  
#     def __init__(self,holdername,age,balance):
#         self.__holdername = holdername
#         self.__age = age
#         self.__balance = balance 
    
#     def showBalance(self):
#         print(f"Available Balance:- {self.__balance}")
    
#     def deposit(self,amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposit Successfully {amount}")
#         else:
#             print("Enter valid amount")
    
#     def withdraw(self,amount):
#         if amount > self.__balance:
#             print("Insufficient Balance")
#         elif amount <= 0:
#             print("Invlid Amount")
#         else:
#             self.__balance -= amount
#             print(f"Withdraw {amount} Successfully, available balance : {self.__balance}")

# # ------- 
# accounts = []

# # --------------- Functions ----------------
# isExit = False
# while not isExit:
#     print("\n==== Mini Bank System ====")
#     print("1  . Create New Account")
#     print("2. Show Account Details")
#     print("3. Deposit")
#     print("4. Withdraw") 
#     print("5. Show Balance")
#     print("6. Exit ")

#     choice = int(input("Enter your choice:- "))

#     if choice == 1:
#         print("====== Create new Account =====")
#         holderName = input("Enter Holde Name:- ")
#         age = int(input("Enter age:- "))
#         balance = float(input("Enter Balance:- "))
#         a1 = BankAccount(holderName,age,balance)
#         obj = {
#             "holderName":a1.__holdername,
#             "age": a1.__age,
#             "balance": a1.__balance
#         }
#         accounts.append(obj)

#     elif choice == 3:
#         print("==== Deposit Amount ====")
#         amount = float(input("Enter amount:- "))
#         acc.deposit(amount)
#     elif choice == 4:
#         print("====== Withdraw Amount ======")
#         amount = float(input("Enter Withdraw Amount:- "))
#         acc.withdraw(amount)
#     elif choice == 5:
#         acc.showBalance()
#     elif choice == 6:
#         isExit = True
#         print("============== Program Ended Successfully ==============")
#     else:
#         print("Please Enter Valid Input")