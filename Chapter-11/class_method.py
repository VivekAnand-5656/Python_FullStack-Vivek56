class Employee:
    a = 56

    @classmethod     # This is class method use for use class methods
    def show(cls):
        print(f"The class attribute of a is {cls.a} ")

e = Employee()
e.a = 85
e.show()