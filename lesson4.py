
# strings

# single quoted string
'This is a string'

'That\'s good'
"That's good"
'That"s good'

# double quoted string
"This is a string"

# triple quoted string
"""This is a string"""



# multiline string

# you can have a multiline strig by appending the \ at the end of each line
'This is the first line'\
    'This is the second line'

# Recommended way to write a multiline string
"""
This is the first line
This is the second line
Another line
"""

# store a string in a variable
name = "Python Lessons"
# print(name)

# combining strings(concatenation)
string_a = "Python" + " " + "Lesson"
print(string_a)

print("Python " + "Lesson")

a = "Python"
b = " "
c = "Lessons"

d = a + b + c
print(d)


# functions for strings
length_a = len(a)
print(length_a)



# define a function that combines 2 strings and outputs the length
def len_of_combination(string1, string2):
    combined_string = string1 + string2
    length = len(combined_string)
    # complex computations

    return length


output = len_of_combination("Python", "Lessons")

print(output)


output2 = len_of_combination(string2="Python", string1="Lessons")
print(output2)
