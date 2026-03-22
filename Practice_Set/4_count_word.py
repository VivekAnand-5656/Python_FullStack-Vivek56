# --- Count words --------
sentence = "Count the number of consonants in a string." 
newSentence = sentence.strip()

count =0
for char in newSentence:
    if char == ' ':
        count+=1

print(newSentence)
count+=1
print("Words is : ",count)
