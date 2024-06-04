# Iterable datatypes: string, list, tuple, set, dict

list = [10, 20, 30, 40, 50]

# for var in list:
#     print(var)

sum = 0

for var in list:
    sum = sum + var
    print(sum)

# Range function = 0 - 999

range (1000)

for var in range (10):
    print(var)

# range start at a specified number and end at a specified number

range (10,100)

for var in range (10,100):
    print(var)

# Range + increment by 5

range (10,100,5)

for var in range (10, 100, 5):
    print(var)

# Sum of first 20 numbers

sum = 0
for var in range (1,21):
    sum = sum + var
    print(sum)

# Search for an element in a list | linear search

list = [10,20,30,40,50,60,70]
key = 45

for var in list:
    if var == key:
        print("Element found")
        break
    else:
        continue
else:
    print("Element not found")
print("Statement after for loop")

# Index of a particular key | At what position value exist | Enumerate

list = [10,20,30,40,50,60,70]
key = 30

for index,var in enumerate(list):
    # print(index,var)
    if var == key:
        print("Element found at index", index)
        break
    else:
        continue
        # Any statement specified after continue will never execute | Code is unreachable
        print("Statement after continue")

else:
    print("Element not found")
# print("Statement after for loop")

# Pass = Used when functionality is not yet defined for a particular block of code | Any statement specified after pass will execute

list = [10,20,30,40,50,60,70]
key = 30

for index,var in enumerate(list):
    if var == key:
        print("Element found at index", index)
        break
    else:
        pass
        print("statement after pass")
else:
    print("Element not found")
