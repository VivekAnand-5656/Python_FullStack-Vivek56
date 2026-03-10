# Python List
# A List is a collection of multiple items stored in a single variable.
# List square brackets [ ] me likhi jaati hai.

numbers = [10, 20, 30, 40]
names = ["Vivek", "Rahul", "Aman"]

print("Numbers : ",numbers)
print("Names : ",names)

# Can be different dataTypes in list

data = ["Vivek", 21, True]
print("Different DataTypes : ",data)

# Access List Elements (Indexing)
# Index 0 se start hota hai.

print("Access by index : ",data[0])

# 1. append() – new item add karta hai
numbers.append(50)
print("Numbers :",numbers)

# remove() – item delete karta hai
numbers.remove(30)
print("Numbers :",numbers)

# insert() – specific position par value add

numbers.insert(2,30)
print("Numbers :",numbers)

# pop() – last item remove karta hai
numbers.pop()
print("Numbers :",numbers)

# sort() – list ko sort karta hai
numbers.sort()
print("Sorted Numbers : ",numbers)

# List: Ordered and mutable collection of items.