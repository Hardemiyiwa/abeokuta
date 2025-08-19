# Control Flow in Python
# A. Conditional Statement
# 1. if statement
age = 20
if age >= 18:
    print("You are eligible to vote")

# some usecases
"""
1. Checking for eligibility
2. Validating login attempts
3. Ensuring a minimum purchase requirement, etc.
"""

# 2. if-else statement
wallet = 400
price = 500

if wallet >= price:
    print("Purchase successful")
else:
    print("Insufficient balance")

# Some usecases
"""
1. Deciding success or failure of a payment.
2. Granting or denying access to a system.
3. Determining pass/fail in an exam.
"""
# 3. if-elif-else
score = 85
if score >= 70:
    print("Grade A")
elif score >= 50:
    print("Grade B")
else:
    print("Grade C")

# Some usecases
"""
1. Student grading systems.
2. Assigning ticket categories (VIP, Regular, Student).
3. Categorizing temperatures(Hot, Warm, Cold), etc
"""

# 4. Nested if
age = 19
citizen = True

if age >= 18:
    if citizen:
        print("You can vote")
    else:
        print("You must be a citizen to vote")
else:
    print("Too young to vote")

# Some usecases
"""
1. Voting eligibility (age + citizenship).
2. Banking (account active + balance sufficient).
3. School admission (age + gade level).
"""

# B. Loops

# 1. for loop
# Iterates through each element in a LIST.
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I like {fruit}")

## Some usecases
"""
1. Iterating through shopping lists.
2. Checking available of products.
3. Displaying student names, etc
"""

# Iterates through each element in a TUPLE. This works like lists, but remember that tuples are immutable

coordinates = (0.34654, -0.48585, 0.57477)
for point in coordinates:
    print(f"point: {point}")

# Some usecases
"""
1. Storing fixed sensor readings.
2. Displaying fixed seating positions, etc
""" 

# Iterates through each element in a DICTIONARY. Remember that dictionaries have key-value pairs.

student = {"name": "Tunde", "age": 16, "grade": "A"}
for key, value in student.items():
    print(f"{key}: {value}")

# some usecases
# Reading database records.
# Showing user profile details.
# Checking configuration settings, etc.

# Iterates through each element in a STRING. Remember that strings are sequences of characters.
word = "PYTHON"
for char in word:
    print(char)

# Some usecases
"""
1. Counting vowels/consonants.
2. Password validation (checking digits/special chars)
3. Text analysis, etc
"""

# 2. While loop
# Using while loop

# Documenting my thoughts
"""
1. Let the loop start with count = 1
2. Let it keep printing until count is greater than 5
3. Let the loop terminate when the condition is no longer true
"""
# My code
count = 1
while count <= 5:
    print("Number:", count)
    count += 1

# Incrementing with while
num = 1
while num <= 10:
    print(num, end=" ")
    num += 1

fruits = ["banana", "mango", "orange"]

for fruit in range(len(fruits)):
    if fruit == len(fruits) - 1:
        print("and", fruits[fruit]) 
    elif fruit == len(fruits) - 2:
        print(fruits[fruit], end=" ")
    else:
        print(fruits[fruit], end=", ")

# Decrementing with while
timer = 10


