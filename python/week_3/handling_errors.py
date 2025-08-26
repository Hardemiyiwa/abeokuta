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
# f = open("missing.txt") # File not found

# Handling Runtime Errors
"""
Python provides exception handling to prevent programs from crashing when unexpected errors occur.
# The Keywords used are:
a. try - block of code to test for errors
b. except - block of code that runs if an error occurs.
c. finally - block of code that always runs (whether error occurs or not).
"""

# The try Block
"""
> It is used to wrap code that might raise an error.
> If no error occurs Python skips the except block.
"""
# try:
#     x = 10 / 2
#     print("Result:", x)

# The except Block
"""
> It defines what to do if an error occurs inside try.
> It can catch specific errors or all errors.
"""

# This is a specific exception
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")

# This is a case of multiple exception
try:
    number = int("abc") # ValueError
    result = 10 / 0     #ZeroDivisionError
except ValueError:
    print("Invalid conversion to integer.")
except ZeroDivisionError:
    print("Cannot divide by zero.")

# The finally Block
"""
If you don't understand this line of code now, It's Ok. But make sure you come back to it once we are done the **File Handling**.
"""
try:
    f = open("sample.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("Closing file if it was opened.")

# Lets have more example on the application of try-except-finally, but try to read in between the line for better understanding.

balance = 5000 # starting balance

print("Welcome to the ATM")
amount = input("Enter amount to withdraw: ")

try:
    amount = float(amount)  # convert input to number

    if amount > balance:
        raise ValueError("Insufficient funds.")
    
    balance -= amount
    print("Withdraw successful. New balance: ₦", balance)

except ValueError as e:
    print("Unexpected error:", e)

finally:
    print("Transaction session closed.")

"""
# If user enters 2000
- Withdrawal successful. New balance: ₦ 3000.0
- Transaction session closed.
"""

"""
# if user enters 6000
- Error: Insuffient funds.
-Transaction session closed.
"""

"""
if user enters abc
- Error: could not convert string to float: 'abc'
- Transaction session closed.
"""

# Semantic Errors
"""
- The code runs without crashing, but the output is logically wrong.
- Hardest to detect because the interpreter see no error.
- Semantic errors are mostly logic mistakes, so subtypes are based on how the logicis wrong.
- Note that semantic errors are not officially exceptions in Python, but they are real mistakes programmers make when logic is wrong.
"""

# Common Subtypes of Semantic Errors
# Wrong Condition in logic

age = 18
if age > 18:    # Should be >=
    print("Eligible to vote")
else:
    print("Not eligible")
# output: Not eligible (wrong result)

# Wrong Formula/Computation
length = 10
width = 5
area = length + width   # should be multiplication
print("Area:", area)

# wrong Variable Usage
marks = [70, 80, 90]
total = marks[0] * marks[1] * marks[2]  # wrong, should be sum
print("Total:", total)
print()