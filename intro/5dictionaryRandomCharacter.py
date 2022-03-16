import random

# create a list of character keys
keys = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]

# create an empty dictionary
dictionaryBeth = {}

# fill the dictionary with list and  random number
for i in keys:
    dictionaryBeth[i] = random.randint(1,20)

# nice print of dictionary
for key in dictionaryBeth.keys():
    print(key, end = " : ")
    print(dictionaryBeth[key])
