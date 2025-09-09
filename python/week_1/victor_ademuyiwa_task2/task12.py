# Simulated USSD Menu Interaction
ussd = input("Welcome to Standard Chartered Bank\nDial *977# to make your transaction: ")
option = input("1. Buy Data\n2. Buy Airtime\n3. Pay Electricity bill\nChoose an option between 1 - 3: ")
print(f"You select option {option}")
amount = float(input("Enter amount: "))
print("Transaction Successful")