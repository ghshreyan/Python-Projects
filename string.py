# We cannot modify the value of a string at the same memory location
# String is ordered data structure | Supports indexing and slicing

# Indexing
# ---------------

# str = "Sample string"
# print(str[3])
# # Starts from right
# print(str[-3])
# # Out of Range
# print(str[100])

# Slicing | end is non-inclusive
# ----------------------------------

str1 = "Sample string 1"
print(str1[0:4])
# Print everything from the 6th index till the end
print(str1[6:])
#Print everything from the beginning till the 8th index
print(str1[:8])

# Stride |
# ------------------

str2 = "Python Sample string"
print(str2[::3])

# Print in reverse
print(str2[::-2])

# Using for loop + slicing

for val in str2[::2]:
    print(val)

# format()
# ------------------

num1 = 100
num2 = 200
print("value of num1 is {} and value of num2 is {}".format(num1,num2))
# Reverse
print("value of num1 is {val2} and value of num2 is {val1}".format(val1=num1,val2=num2))

# capitalize() = Converts the first letter of the string to Capital
# ----------------------------------------------------------------------

s = "Python string"
s1 = s.capitalize()
print(s1)

# upper() = converts the entire string to upper case | lower() = converts the entire string to lower case |
# title() = converts first character of every work to upper case
# ----------------------------------------------------------------------------------------------------------------

u = "python string in upper case"
print(u.upper())
print(u.lower())
print(u.title())

# isupper() = checks whether the given string is in upper case or not | Returns true/false
# islower() = checks whether the given string is in lower case or not | Returns true/false
# istitle() = checks whether the given string has the first letters of every word in capital or not | Returns true/false
# --------------------------------------------------------------------------------------------------------------------------

u1 = "python string in upper case"
print(u1.isupper())
print(u1.islower())
print(u1.istitle())

# split() = splits a string based on a delimiter and converts to a list |
# --------------------------------------------------------------------------------

string = "PYTHON,CSS,HTML,JAVA,DJANGO"
# splits based on the delimiter=","
print(string.split(","))
# In case the given delimiter is not present, it still converts the string to a list but entire list will be one element
print(string.split(" "))

# join() = joins a list based on a delimiter
# ------------------------------------------------

string_join = ("|").join(string)
print(string_join)

# maketranse | translate = transform a string based on a particular mapping
# --------------------------------

m1 = "1234"
m2 = "abcd"
m3 = "Python sample string abcd "

table = str.maketrans(m2,m1)
result = m3.translate(table)
print(result)

# index() = returns the index of the specified string | case-sensitive | returns the index first occurrence |
# starts traversing from the left hand side
# ------------------------------------------------------------------------------------------------------------

i = "INDEX,HTML,PYTHON,PYTHON,PYTHON"
print(i.index("PYTHON"))

# find() = returns the index of the specified string | returns -1 if something is specified that doesn't exist
# rfind ()= returns the index of the specified string but starts traversing from the right hand side
# -----------------------------------------------------------------------------------------------------------------

print(i.find("PYTHON"))

print(i.rfind("PYTHON"))

# strip() = removes the specified element from the left and right hand side
# lstrip() = removes the specified element from the left hand side
# rstrip() = removes the specified element from the right hand side
# ---------------------------------------------------------------------------------


strp = "******This is a sample string******"
print(strp.strip("*"))
print(strp.lstrip("*"))
print(strp.rstrip("*"))

# center() = appends the specified element around the string by keeping the string in the center
# ljust() = appends the specified element on the left hand side of the string
# rjust() = appends the specified element on the right hand side of the string
# --------------------------------------------------------------------------------------------------

cen = "PYTHON"
print(cen.center(20,"*"))
print(cen.ljust(20,"*"))
print(cen.rjust(20,"*"))

# replace() = replaces the specified string with another string
# -------------------------------------------------------------------

rep = "python,CSS,HTML,perl,ruby"
print(rep.replace("HTML","HTML5"))


