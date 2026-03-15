# ------ Exception Handling ------
# --- try - except ----
try:
    a =10
    b=5
    print(a/b)
except Exception as e:
    print(e)

# --- Specific Exception ----
try:
    a = 10
    b = 0
    print(a/b)
except ZeroDivisionError:
    print("Can not divide by 0")

# Multiple Exceptions

try:
    num = int(input("Enter a number " ))
    print(10/num)
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Can not divide by 0")

# ----- else Block ---
try:
    a = 10
    b = 2
    print(a / b)

except ZeroDivisionError:
    print("Error")

else:
    print("Division successful")

# ------------ finally Block ------
try:
    print(10 / 2)

except:
    print("Error")

finally:
    print("Program finished")

# ---------- Custom Exception Raise karna -------

age = 15
if age < 18:
    raise Exception("Age must be 18+")