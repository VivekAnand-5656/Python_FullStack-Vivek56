# A string is a sequence of characters
name = "Vivek Anand"
city = "Deoghar"

print(name)
print(city)

# 2. Access Characters in String (Indexing)
# Each character in a string has an index number starting from 0.

print(name[0])
print(name[3])

# 3. String Length
# Use len() function.

length = len(name)
print("Length of name : ",length)

# 4. String Concatenation (Join Strings)

message = "Hello "+name+" your city is "+city
print("Concatenation : ",message)

# 5. String Methods
# Convert to Uppercase/

word = "vivek"
print("UpperCase : ",word.upper())

word2 = "VIVAN"
print("LoweCase : ",word2.lower())

# Replace Text

text = "Hello World"
print("Replace : ",text.replace("World","Python"))

# 6. Multi-line String
# Use triple quotes.

poem = '''
Repeatedly October descends
On villages     deep rivers     jungles
Waiting and silence
Asphyxia and union
Repeatedly the sky’s autumn turns its head
Towards the meat of greed

Village roots     bodies     songs
Roads     festivals     waterlessness
Have unfurled before them existence
And into their mouths descends
The shadowfree meat of October

This is our Bangla, woken up again
By the unaccustomed sound of other languages
Though even now the meat of a few old phrases still clings

The uprooting of a multitude of villages can clearly be heard
Day of incredible sun, phrases worn out by disuse
Goodbye messages in an unaccustomed language
Pages of grammar spiked on nails
Rising in grotesque metallic sound

The uprooting of years and days can be heard
Catatonia comes and touches wholeness
Meat-eating birds can be seen
Tearing hunks from the flesh of massive villages
The bodies of massive rivers

Village and town      practise and partition     could clearly be heard
Prepared reading lists and repudiation
Boycotted words and my own-ness
Uprooting of that fixed gazing towards the stars

Thousands of meat-eating birds were heard
Who in truth are carrying away crematoria and carrion-dumps
from chockful skies
Carrying away the mounds of our neglect

Have they taken me too? The entire sky is the belly
Of a snake swollen with villages swallowed whole
Leaving behind
The sloughed-off skin of my language    unlettered
'''
# print("Poem : ",poem)

# 7. Check String Type
print("String type : ",type(name))

# ✅ Short Definition (Exam / Interview)
# A string in Python is a sequence of characters enclosed in quotes used to store text data.