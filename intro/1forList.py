
print("test the github and VSC！")

# in a zoo
zoolist = ["dog", "cat", "bird", "horse", "tiger", "snake", "monkey", "sheep", "mouse", "rabbit", "deer"]

# the first way to print list
print(zoolist)

# the second 
print("There are some ")
for animals in zoolist:
    print(animals, end =" ")

# the third 
print()
print("There are", len(zoolist), "kinds of animals.")
for i in range(len(zoolist)):
    print("This is a " + zoolist[i])