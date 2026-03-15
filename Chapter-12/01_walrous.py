# 1 - Walrus Operator
# 2 - Types Defination
# 3 - Match Case


# ----- Walrus Operator ----
# We called it also Assignment Operator 
# Use to this value is assign and return in one line
if (name := input("Enter name:- ")) and len(name) >5:
    print(name)
else:
    print("Name is too short")

# ------ Types Defination -----------
# “This makes the code more readable and helps the IDE understand what the variable’s type is.”

username: str = "vivek@56"
age: int = 22
price: float = 299

# ---- In Function ----
def add(a:int,b:int) -> int: # -> it means return integer type function
    return a+b

print(add(5,6))

# --- List Type ---
numbers: list[int] = [1,2,3,4,5]
print("numbers: ",numbers)

# ----- Dictionary Types ----
data: dict[str,int] = {
    "a":1,
    "b":5
}
print("Dict :- ",data)

# ---- Match Case ---
 

def weekdays(day):
    match day:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case _:
            return "Other Day"

print("Result : ",weekdays(3))

