# Arithmetic Operators = +, -, *, /, //, %, **

# Addition

num1 = 5
num2 = 10

sum = num1 + num2
print(sum)

# Substraction

num1 = 5
num2 = 10

print(num2 - num1)

# Multiplication

num1 = 5
num2 = 10

print(num1 * num2)

# Division (If division operator is used, we'll always get a floating point result) | true-division

num1 = 5
num2 = 10

print(num2 / num1)

print(10 / 3)

# Floor Division | returns the integer part of the output

print(10 // 3)

# Mod | returns the remainder part of the output

print(10 % 3)

# Power (to the power)

print(10 ** 2)

# --------------------------------------
# Comparison Operators = <, >, <=, >=, ==, != | Always returns "true" or "false"

# Equal |  Not Equal

    # Returns true if values are same
var1 = 10
var2 = 50

    # Equal
print(var1 == var2)

    # returns false if values are different
var3 = 10
var4 = 10

print(var3 == var4)

    # Not-equal
print(var1 != var2)

# Greater than | Less than | Greater-than-equal | less-than-equal

var5 = 10
var6 = 5

    # Greater than
print(var5 > var6)

    # Less than
print(var5 < var6)

    # Greater-than-equal

print(var5 >= var6)

    # less-than-equal

print(var5 <= var6)

# --------------------------------
# Identity Operators = is, is not | compares memory location

num7 = 100
num8 = 100

print(num7 == num8)
print(num7 is  num8)

list1 = [1,5,10,20]
list2 = [1,5,10,20]

print(list1 == list2)
print(list1 is list2)
print(list1 is not list2)

# -------------------------------------
# Assignment operators = =, +=, -=, *=, /=

# = is used to assign a value to a variable

num9 = 5

print(num9 + 5)

num9 += 10
print(num9)

num9 -= 2
print(num9)

# -------------------------------------------
# Bitwise operators = &, |, ^, >>, <<

num11 = 5
num12 = 10

print(bin(num11), bin(num12))

print(num11 & num12)

print(num11 | num12)

print(num11 >> num12)

print(num11 << num12)

# -------------------------------------
# Logical Operators = and, or, not

    # and | Will return true if both conditions are true
print(10 == 10 and 20 == 20)

print(10 == 16 and 20 == 20)

    # or | will return true if any one condition is true

print(10 == 16 or 20 == 20)

print(10 == 16 and 20 == 21)

    # not | returns the opposite of true (if true) or false (if false)

print(not (10==15))

print(not (10==10))

# -----------------------------------------
# Membership Operators = in and not in

list3 = [1,2,5,10,20,40]

print(10 in list3)

print(100 in list3)

string = "Python string"

print("Python" in string)

print("Python" not in string)

print("python" not in string)