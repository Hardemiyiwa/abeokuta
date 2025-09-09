# Create and Display
# accepting users input
dish1 = input("Enter your first favourite dishes: ")
dish2 = input("Enter your second favourite dishes: ")
dish3 = input("Enter your third favourite dishes: ")

# Creating tuple
dishes = (dish1, dish2, dish3)

# printing tuple in a single
print(dishes)

# printing each dishes in single line using \n
print("\n".join(dishes))
# Or
print(f"{dishes[0]}\n{dishes[1]}\n{dishes[-1]}")