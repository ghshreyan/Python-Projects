var1 = 5
var2 = 10
addition = var1 + var2
print(addition)

# Print the datatype for the above variables

print(type(var1),type(var2))

# Print the memory location for the above variables

print(id(var1),id(var2))

# Object intering = If you define two different objects having the same value, Python will not create two different object/variable

a = 10
b = 10

print(id(a),id(b))