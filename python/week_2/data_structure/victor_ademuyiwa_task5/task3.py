# Tuple Operation
# collecting user input 
state1 = input("Enter the first state: ").lower()
state2 = input("Enter the first state: ").lower()
state3 = input("Enter the first state: ").lower()
state4 = input("Enter the first state: ").lower()
state5 = input("Enter the first state: ").lower()

# Storing the data in collected in a tuple
nigeria_state = (state1, state2, state3, state4, state5)

# printing the first and the last
print(f"first state {nigeria_state[0]}")
print(f"last state {nigeria_state[-1]}")

# checking if lagos in the state
print("lagos" in nigeria_state)

# printing number of state entered
print(len(nigeria_state))

