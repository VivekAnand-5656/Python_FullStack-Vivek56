
# =========> OOP(Object Oriented Programming) <============

class Employee:
    name = "Vivek Anand" # This is a class attribute
    language = "Python"
    salary = 120000

vivek = Employee() #  vivek is an object
vivek.company = "TCS" # This is an object/instance attribute
print(f"Employee Name : {vivek.name}")
print(f"Employee Language : {vivek.language}")
print(f"Employee Salary : {vivek.salary}")
print(f"Employee Company : {vivek.company}")