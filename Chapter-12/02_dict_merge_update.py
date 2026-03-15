# 4 - Dictionary Merge & Update Operators (Python 3.9)
# --- Merge Operator ---- (|) merge two dicts ---
a = {
    "x":1,
    "y":2
}
b = {
    "z" :5
}
c = a | b
print("Merged Dict : ",c)
# ---- Update Operator --- (|=) Update Existing Dictionary ----
first = {
    "a":5,
    "b": 6
}
second = {
    "c":8,
    "d":9
}
first |= second
print("Updated Dict : ",first)
