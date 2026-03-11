# 2. Python Set
# A Set ek collection hai jisme unique values hoti hain.
# Duplicate values allowed nahi
# Order fix nahi hota

numbers = {1,2,3,4,4,5} # Duplicates Automatically Removed 
print("Set : ",numbers)
print("Type: ",type(numbers))

# 2. Set Create Karna
# Empty set , ⚠️ {} empty dictionary hota hai, set nahi.
s = set()

# 3. Access Set Elements
# Set unordered hota hai, isliye indexing nahi hoti.

for i in numbers:
    print(i)

# 1. add()
# Set me single element add karta hai.

numbers.add(6)
print(numbers)

# update()
# Ek se zyada elements add karta hai.

numbers.update([7,8,9])
print(numbers)

# update()
# Ek se zyada elements add karta hai.

numbers.remove(8)
print(numbers)

# discard()
# Element remove karta hai but error nahi deta.

numbers.discard(9)
print(numbers)

# pop()
# Random element remove karta hai.

numbers.pop()
print(numbers) 

# clear()
# Set ke saare elements delete kar deta hai. ---- Output :- set()

numbers.clear()
print(numbers)

# Mathematical Set Operations (Very Important)
# 7. union()
# Do sets ko combine karta hai.
a = {1,2,3}
b = {4,5,3}
print(a,b)
print("Combo : ",a.union(b))

# intersection()
# Common elements nikalta hai.

print(a.intersection(b))

# difference()
# First set me jo element hai aur second me nahi.

print(a.difference(b))

# issubset()
# Check karta hai ek set dusre ka subset hai ya nahi.

num = {1,2}
num2 = {1,2,3,4}

print(num.issubset(num2))


