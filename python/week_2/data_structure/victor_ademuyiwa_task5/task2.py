# Tuple and Input
# collecting user input 
friend1 = input("Enter your first best friend name: ")
friend2 = input("Enter your second best friend name: ")
friend3 = input("Enter your third best friend name: ")
friend4 = input("Enter your fourth best friend name: ")
friend5 = input("Enter your fifth best friend name: ")

# Storing the collected data in a tuple
friends = (friend1, friend2, friend3, friend4, friend5)
reversed_friends = friends[::-1] 
print(reversed_friends)