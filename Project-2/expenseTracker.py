# ========== Expense Tracker =========
expenses = []

isExit = False

while isExit == False:
    print("\n==== Expense Tracker ====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spending")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter amount : "))
        catagory = input("Enter catagory: ")
        expense = {
            "amount": amount,
            "catagory": catagory
        }
        expenses.append(expense)
        print("Expense add Successfully!")
    elif choice == 2:
        if len(expenses) == 0:
            print("No Expense found")
        else:
            print("===== Your Expenses =====")
            for exp in expenses:
                print("Ammount : ",exp["amount"]," Catagory: ",exp["catagory"])
    elif choice == 3:
        total = 0 
        for exp in expenses:
            total += exp["amount"]
        
        print("Total Spending : ",total)
    elif choice == 4:
        isExit = True
        print("Exit Successfully")
    else:
        print("Please Enter valid input")