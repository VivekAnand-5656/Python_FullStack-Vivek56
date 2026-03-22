word = input("Enter a word: ") #   --------- Check Palindrom --------------
rev = word[::-1]
if word == rev:
    print(True)
else:
    print(False)