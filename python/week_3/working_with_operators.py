# Python Operators
# Comparison Operators
a = 10
b = 20

print(a == b)   # False
print(a != b)   # True
print(a > b)    # False
print(a < b)    # True
print(a >= 10)  # True
print(b <= 25 ) # True

# Use case Example- Student Exam Result
score = 75

print(score >= 50)  # True (Passed)
print(score < 50)   # False (Failed)
print(score == 100) # False (Not full marks)

# Assignment Operators
x = 10
print("Initial value:", x)

x += 5
print("After x += 5:", x)

x -= 2
print("After x -= 2:", x)

x *= 3
print("After x *= 3:", x)

x /= 4
print("After x /= 4:", x)

x %= 3
print("After x %= 3:", x)

x = 4
x **= 2
print("After x **= 2:", x)

x //= 3
print("After x //= 3:", x)

# Use case Example:

# Define variables
balance = 1000
deposit = 200
withdraw = 150

balance += deposit  # Add deposit
balance -= withdraw # Subtract withdrawal

print("Updated Balance:", balance)
# Output: Updated Balance: 1050

# Logical Operators
x = 10
y = 20

# and operator
print(x > 5 and y > 15) # True

# or operator
print(x < 5 or y > 15)  # True

# not operator
print(not(x == 10))     # False

# Use case example1 - Scholarship Eligibility

# Define variable
age = 17
score = 85

# Must be younger than 18 AND score above 80
eligible = (age < 18) and (score > 80)

print("Scholarship Eligible:", eligible)
# Output: Scholarship Eligible: True

# Use case example2 - Event Access
age = 22
has_ticket = False

can_enter = (age >= 18) and (has_ticket or age < 25)

print("Acess Granted:", can_enter)
# Output: Acess Granted: True (because age < 25 even without ticket)