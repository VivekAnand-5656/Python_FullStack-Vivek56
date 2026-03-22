# ========= Capitalize words of first char of words ===========
sent = "python is powerful programming"
result = ""
new_word = True
for ch in sent:
    if ch == " ":
        result += ch
        new_word = True
    else:
        if new_word:
            result += ch.upper()
            new_word = False
        else:
            result += ch.lower()
print(sent)
print(result)