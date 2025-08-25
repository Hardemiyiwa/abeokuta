# Handling Errors in Python
"""
# Errors in python are classified into three main categories:
1. Syntax Errors
2. Runtime Errors
3. Semantic Errors
"""

# Syntax Errors
"""
1. It occur when the python interpreter cannot understand your code because it breaks python grammar rules.
2. Please note that Program will not run until the error is fixed.
"""
# Common Subtypes of Syntax Errors
# a. IndentationError - Incorrect spacing
# for i in range(3):
# print(i) # Wrong identation
# This will through error except you fix the identation

# b. Missing Colon/Parenthesis Error
# if 5 > 3 #Missing colon
    # print("Hello")

# c. Invalid Syntax - General grammar mistakes
# print "Hello" # Missing parentheses in python 3

# Runtime Errors
"""
1. The program is syntactically correct, but an error
2. These are also called exceptions.
3. They can be handled with try, except, and finally 
"""
# Common Subtypes of Runtime Errors
# a. ZeroDivisionError - Dividing by zero.
# x = 10 /0 # This will throw error

# b. NameError - Using a variable before defining it.
# print(age) # age not define

# c. TypeError - Wrong data type in an operation.
# result = "10" + 5 # str + int not allow

# d. ValueError - Invalid value for a function.
# number = int("abc") # cannot convert string to int

# e. IndexError - Accessing list index out of range.
# fruits = ["apple", "banana"]
# print(fruits[3]) # Index out of range

# f. KeyError - Accessing a dictionary with a missing key.
# data = {"name":   "Ada"}
# print(data["age"]) # Key not found

# g FileNotFoundError - File does not exist.
f = open("missing.txt") # File not found

# Handling Runtime Errors
"""
Python provides exception handling to prevent programs from crashing when unexpected errors occur.
# The Keywords used are:
a. try - block of code to test for errors
b. except - block of code that runs if an error occurs.
c. finally - block of code that always runs (whether error occurs or not).
"""

# The try Block
