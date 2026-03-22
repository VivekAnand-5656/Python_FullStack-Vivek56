student = {
    "name" : "Vivek Anand",
    "age" : 21,
    "city" : "Delhi"
}
student["course"] = "Python" 
student["age"] = 22
print(student)
del student["course"]


print(student)
for key in student:   # print keys
    print(key)

for value in student.values():   # print values
    print(value)
 
for key, value in student.items():   # key and value print
    print(key," ",value)

# ------ count of keys ---
key_count = len(student)
print("Number of key :",key_count)