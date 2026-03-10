# 1. Python Dictionary
# A Dictionary ek key–value pair data structure hai.
# Isme data { } curly brackets me store hota hai.

student = {
    "name" : "Vivek Anand",
    "age" : 21,
    "course" : "Python"
}
print("Student Data :",student)
print("Student Name :",student["name"])
print("Student Age :",student["age"])

# Important Dictionary Methods
# 1. get()
# Safe way to access value.

print("Student get Course : ",student.get("course"))

# 2. keys()
# Dictionary ke saare keys return karta hai.

print("Student Keys : ",student.keys())

# 3. values()
# Dictionary ke saare values return karta hai.

print("Student values : ",student.values())

# 4. items()
# Key + value pair return karta hai.

print("Key value pairs : ",student.items())

# 5. update()
# Dictionary ko update karta hai.

student.update({
    "age" : 22
})
print("Updated Student :",student)

# 6. pop()
# Specific key remove karta hai.

student.pop("age")
print("Delete age key : ",student)

# 7. clear()
# Dictionary empty kar deta hai.

student.clear()
print("Cleared Dict :",student)
