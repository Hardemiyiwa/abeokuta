# Basic usage of input()
name = input("Enter your name: ")
print("Hello,", name)

# Convert input to integer
age = int(input("Enter your age: "))
print(f"You will be {age + 1} years old next year.")

# Calculator using input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
sum_result = num1 + num2
print(f"The sum of {num1} and {num2} is {sum_result}")

# Taking order
# Step 1: Welcoming the customers
# Step 2: Asking the user for his or her order
# Step 3: Displaying the user order
print("Welcom to NCC resturant")
customer_order = input("What is your order for today? ")
print('Here is your order:', customer_order)