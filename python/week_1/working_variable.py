# account_name = "Ridwan" # users acount name
# year_of_birth = 2006 # user year of birth
# weekly_wages = 99,999.99 # user weekly wages
# print(f"mr.{account_name}, your weekly wages is {year_of_birth}")

# type casting
# int()
# float()
# str()
# bool()

# Convert input to integer
# age = int(input("Enter your age: "))
# print(f"You will be {age + 1} years old next year.")

# Calculator using input
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# sum_result = num1 + num2
# print(f"The sum of {num1} and {num2} is {sum_result}")

# Using using ussd code to check data balance
# using input to collect the code
# print the balance option
# showing the balance

code = input("Enter your \"ussd code\"(using \"*323#\"): ")
options = int(input("1. Access plan balance\n2. Business plan balance\n3. Broadband balance\n4. Balance check"))
print("Dear customer, you don't have any active data bundle.\nPlease dail \"*312*1#\" to buy another another data bundle\n") 