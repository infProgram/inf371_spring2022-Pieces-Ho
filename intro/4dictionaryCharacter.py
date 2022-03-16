characterAlice = {'Strength':12, 'Dexterity':13, 'Constitution':9, 'Intelligence':2, 'Wisdom':6, 'Charisma':18}

# print the entire dictionary
print(characterAlice)

# print the dictionary by for-loop
for key in characterAlice:
    print(key, end = "  ")
print()

# Test if 'Strength' in character dictionary
if 'Strength' in characterAlice:
    print("The Strength is ", characterAlice['Strength'])
else:
    print("Strength is not a character stat.")

# Test if 'Speed' in character dictionary
if 'Speed' in characterAlice:
    print("The Speed is ", characterAlice['Speed'])
else:
    print("Speed is not a character stat.")