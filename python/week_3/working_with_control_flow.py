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
"""
1. Reading database records.
2. Showing user profile details.
3. Checking configuration settings, etc.
"""

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
while timer > 0:
    print("Countdown:", timer)
    timer -= 1

# while with User Input
# Keep asking until the user enters a correct password.
password = ""
while password != "python123":
    password = input("Enter the password: ")

print("Access Granted!")

# understanding while True
"""
. The while True: loop is an infinite loop - it keeps running forever until you explicity stop it with a break statement or by exiting the program
. It is commonly used when:
a. you don't know in advance how many times you want the loop to run.
b. you want to keep asking the user for input until a valid condition is met
c. You are building continuous programs like menus, login systems, or simulations.

while True:
    # code block
    # Must include a breake statement to stop
"""

# Keep asking the user for a name until they type "exit".

while True:
    name = input("Enter your name (type 'exit' to quit): ")
    if name.lower() == "exit":
        print("Goodbye!")
        break
    print(f"Hello, {name}")

# Useful in chat-like applications, forms, or data entry programs where users may input multiple times until they decide to stop.

# Loop control statements (break, continue and pass)
# 1. break
for num in range(1, 10):
    if num == 5:
        break
    print(num)
"""
# The loop stops completely when num == 5.
# Stop searching when an item is found.
# Exit when user input matches a condition.
# Prevent Unnecessary iterations.
"""

# 2. Continue
for num in range(1, 6):
    if num == 3:
        continue
    print(num)
"""
# 3 is skipped, but the loop continues.
# Some usecases
1. Skip invalid data.
2. Ignore unwanted characters (like spaces in a string).
3. Continue running buh avoid certain cases, etc.
"""

# 3. Pass
# Does nothing, A placeholder to avoid errors. It is used if you haven't written the code yet but want to keep the structure.
for num in range(1, 6):
    if num == 3:
        pass # do nothing for now
    else:
        print(num)
"""
# At num == 3, Python executes pass (nothing happens).
# Some usecases
1. Writing code structure (to fill later)
2. Placeholders in class/method definitions.
3. Temporarily disable parts of code.
"""

while True:
    print("\nMenu:")
    print("1. Say Hello")
    print("2. Say Goodbye")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("Hello")
    elif choice == "2":
        print("Goodbye")
    elif choice == "3":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.")

# Try and use while True for validation
while True:
    age = input("Enter your age: ")
    if age.isdigit():
        print(f"Your age is {age}")
        break
    else:
        print("Invalid input. Please enter a number.")

# lets make a guess
secret = "python"

while True:
    guess = input("Guess the secret word: ")
    if guess.lower() == secret:
        print("Correct! You guessed the word.")
        break
    else:
        print("Wrong")

# Do you remember this?

balance = 1000

while True:
    print("\nATm Menu:")
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print(f"Your balance is: {balance}")
    elif choice == "2":
        amount = int(input("Enter withdrawal amount: "))
        if amount <= balance:
            balance -= amount
            print(f"Withdrawal successful. New balance: {balance}")
        else:
            print("Insufficient funds.")
    elif choice == "3":
        print("Thank you for using our ATM. Goodbye!")
        break
    else:
        print("Invalid option. Try again.")