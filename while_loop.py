# While is preferred when there is a specific condition to check | It always returns true or false

# while [condition]:
#     [statements]
# else:

# Print sum of first 20 numbers using while loop

count = 1
sum = 0

while count <= 20:
    sum = sum + count
# Make sure to include a statement to increment the count, else it will go into an infinite loop
    count = count + 1
print(sum)
