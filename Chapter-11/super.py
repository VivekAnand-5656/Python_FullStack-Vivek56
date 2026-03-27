# ============ Multilevel Inheritance ===============

class Employee:
    def __init__(self):
        print("Constructor of Employee")
    name = "Vivek Anand"

class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
    programmerName = "Shaurya Kumar"

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")
    managerName = "Arun Jetali"   # This can access all

a = Employee()
b = Programmer()
c = Manager()  

print(c.programmerName)
