# 1. Simple if Condition
# The if statement checks a condition.

age = 20
if age >= 18:
    print("You can vote")

# 2. if-else Condition
# Used when there are two possible outcomes.

num = 18
if num % 2 ==0:
    print("Even")
else:
    print("Odd")

# 3. if-elif-else Condition
# Used when there are multiple conditions.

marks = 75
if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")

# 4. Nested if (Important for Logic)
# if ke andar ek aur if use kar sakte hain.

citizen = True
if age >= 18:
    if citizen:
        print("Eligble for vote")
else:
    print("Not Eligble for vote")


# 5. Short Conditional Expression (Ternary Operator)
# Python me one-line condition bhi likh sakte hain.

result = "Adult" if age >= 18 else "Minor"
print(result)

# 6. Logical Operators in Conditions
# Operator	Meaning
# and	dono condition true
# or	koi ek true
# not	opposite;   

# ---- and -----
if age >= 18 and citizen:
    print("Eligble for PAN")
else:
    print("Not Eligble")

# ----- or -----
has_Permission = True
if age >= 18 or has_Permission:
    print("You can Enter")
else:
    print("Can not Enter")

# ----- not -----
isLoggedIn = False
if not isLoggedIn:
    print("Please login")
