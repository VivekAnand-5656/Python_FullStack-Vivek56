

class Employee:
    language = "Python"
    salary = 1200000
    def __init__(self,name,salary,language):   # dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language

    def getInfo(self): 
        print(f"The language is {self.language} and Salary is {self.salary} ")
    
    def greet(self):                # ----- self is must importand whatever we use or not use 
        print("Good Morning")
    
    # ---- if we do not use self and do not want to pass object --
    @staticmethod
    def msg():
        print("We did not pass any complete object")
    
vivek = Employee("Vivek",1300000,"Java")
print(vivek.name,vivek.salary,vivek.language)
# # vivek.getInfo() 
# Employee.getInfo(vivek) 
# vivek.greet()
# vivek.msg() 

 