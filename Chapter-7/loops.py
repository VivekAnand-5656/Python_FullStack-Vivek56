# Python mainly has two types of loops:
# for loop
# while loop

# --------- for loop --------
# A for loop is used when you want to iterate over a sequence like a list, string, tuple, or range.

for i in range(1,6):
    print(i)

# Loop through a list
names = ["Vivek","Karan","Kritika"]
for name in names:
    print(name)

# Loop through a string
course = "Python"
for char in course:
    print("Char : ",char)

# ----------- while Loop -------
# A while loop runs as long as the condition is True.

i =1
while i<= 5:
    print(i)
    i+=1
    