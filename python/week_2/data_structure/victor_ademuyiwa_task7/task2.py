# Super Market Price List
# creating an empty dictionary
store_items = {}
# List of an item 
items = ["cloth", "shoe", "watch", "boxers", "belts"]
for i in range(len(items)):
    store_items.update({
        items[i]: float(input(f"Enter the price of {items[i]} in: "))
    })
print(f"Available items and their price\n{store_items}")

# Available items
print(f"Available items: {" ".join(store_items.keys())}")

# update items 
update_item = input("Enter the item you want to update: ").lower()
if update_item in store_items.keys():
    store_items[update_item] = float(input(f"Enter the price of  {update_item}: "))
else:
    print(f"{update_item} is not among the item")
print(store_items)