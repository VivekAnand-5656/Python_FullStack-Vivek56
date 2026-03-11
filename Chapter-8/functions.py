
def avg ():
    a =int(input("Enter a number : "))
    b =int(input("Enter b number : "))
    c =int(input("Enter c number : "))

    total = (a+b+c)/3
    print("Average : ",total)

# avg()

def message():
    name = input("Enter your name : ")
    print("Welcome to Python Journey : ",name)

# message()

def goodDay(name):
    print("Good Day : ",name)

goodDay("Vivek")

# ----- Return Value ---
def isLogin(dir):
    if dir:
        return "Login Successfull"
    return "Try Again"

ok = isLogin(False)
print(ok)

# ------------ Default Parameter Value ---------
def goodMorning(name,ending="Wak-Up"):
    print(f"Good Morning :",name,ending)

goodMorning("Vivek")
goodMorning("Khushi","Go for Walk")
# ------------ Left Recursion -------------