# --------- Count Vowels ------------
word = "vivek raut kumar ji ki jay ho"
vowel = 0
cons = 0
for char in word:
    if char == 'a' or char == 'A' or char == 'e' or char == 'E' or char =='i' or char == 'I' or char == 'o' or char == 'O' or char == 'u' or char == 'U':
        vowel+=1
    elif char == ' ':
        continue
    else:
        cons+=1
    
print("Vowels : ",vowel)
print("Consonant : ",cons)