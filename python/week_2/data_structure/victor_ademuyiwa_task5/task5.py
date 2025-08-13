# Modify Tuple indirectly
# collecting users shopping list
shopping1 = input("Enter the first item on your shopping list: ")
shopping2 = input("Enter the second item on your shopping list: ")
shopping3 = input("Enter the third item on your shopping list: ")

# storing collected data in to tuple shopping list
shopping_list = (shopping1, shopping2, shopping3)

# converting to list
list_shopping_list = list(shopping_list)

# Asking for two more items
list_shopping_list.append(input("Enter the fourt item on your shopping list: "))
list_shopping_list.append(input("Enter the fifth item on your shopping list: "))

# converting back to tuple
shopping_list = tuple(list_shopping_list)
print("|".join(shopping_list))