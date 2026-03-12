# ----------------- Inheritance -----------

class Employee:
    company = "ITC"
    name = "Vivek Anand"
    salary = 120000
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary} ")

class Data:
    storename = "Vivek Store"

class Programmer(Employee,Data):
    company = "ITC Infotech"
a = Employee()
b = Programmer()


print(a.company," - ",b.company)
print(b.show())
print(b.storename)