num1 = 700
num2 = 700

if num1 > num2:
    print("num1 is greater than num2")
elif num2 > num1:
    print("num2 is greater than num1")
else:
    print("Both are equal")

# -----------------------------------
# If a non-zero value is specified, by default it is considered as true

if 0:
    print("Statement in if block")
else:
    print("Statement in else block")