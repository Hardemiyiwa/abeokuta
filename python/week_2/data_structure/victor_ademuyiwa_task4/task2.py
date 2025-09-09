# Shopping List Manager
shopping_list = []
# accepting user's shopping items
first_item = input("Enter you first shopping item: ")
second_item = input("Enter you second shopping item: ")
third_item = input("Enter you third shopping item: ")
# Adding the user's item to the shopping list
shopping_list.append(first_item)
shopping_list.append(second_item)
shopping_list.append(third_item)
# Displaying the shopping list
print(shopping_list)
print(f"Shopping list: {shopping_list[0]}, {shopping_list[1]}, {shopping_list[-1]}")
print(f"shopping list: {", ".join(shopping_list)}")