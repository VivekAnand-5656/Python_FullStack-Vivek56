# --------------------- Practice ----------------
class Student:
    def __init__(self,name,age,course):
        self.name = name
        self.age = age
        self.course = course
     

# ----- File ----
fileName = "student.txt"
def add_student_file(std):
    with open(fileName,"a") as file:
        file.write(f"{std.name},{std.age},{std.course}\n")

def load_students_from_file():
    studentsList = []  
    try:
        with open(fileName,"r") as file:
            for line in file:
                name, age, course = line.strip().split(",")
                students.append({
                    "name": name,
                    "age": age,
                    "course": course
                })
    except FileNotFoundError:
        pass
    return studentsList

students = load_students_from_file()
isExit = False
while not isExit:
    print("\n==== Student Management ====")
    print("1. Add Student")
    print("2. View Student")
    print("3. Total Student")
    print("4. Exit")

    userInput = int(input("Enter your choice:- "))
    if userInput == 1:
        print("====== Add Student ======")
        userName = input("Enter your name:- ")
        userAge = int(input("Enter your age:- "))
        userCourse = input("Enter your course:- ")
        s1 = Student(userName,userAge,userCourse)
        obj = {
            "name" : s1.name,
            "age" : s1.age,
            "course" : s1.course
        }
        students.append(obj)
        add_student_file(s1)
        print("---- Studetn Addedd Successfully ------")
    elif userInput == 2:
        print("===== All Students =====")
        for student in students:
            print(f"Name: {student['name']}, Age: {student['age']}, Course: {student['course']}")
    elif userInput == 3:
        print("==== Total Students ====")
        size = len(students)
        print(f"Total :- {size} ")
    elif userInput == 4:
        isExit = True
        print("--- Program Ended Successfully ----")
    else:
        print("Please Enter Valid Input")
