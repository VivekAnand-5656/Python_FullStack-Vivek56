# ============ Multilevel Inheritance ===============

class Employee:
    name = "Vivek Anand"

class Programmer(Employee):
    programmerName = "Shaurya Kumar"

class Manager(Programmer):
    managerName = "Arun Jetali"   # This can access all

a = Employee()
b = Programmer()
c = Manager()
print("Employee access :- Employee Name : ",a.name)
print("Programmer access :- Programmer Name : ",b.programmerName," Employee Name :",b.name)
print("Manager access :- Manager Name : ",c.managerName," Programmer Name : ",c.programmerName," Manager Name : ",c.name)