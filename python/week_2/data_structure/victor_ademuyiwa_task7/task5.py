# Contact Quick Loookup
name = ("Tolu", "Wale", "Yinka")
phone_no = ("08147894567", "09154678943", "09034678923")
# Combining the name and phone
name_phone_list = list(zip(name, phone_no))
# Creating a dictionary
phone_list = {}
phone_list.update({
    name_phone_list[0][0]: name_phone_list[0][1],
    name_phone_list[1][0]: name_phone_list[1][1],
    name_phone_list[-1][0]: name_phone_list[-1][1]
})

# Asking User for a name
phone_name = input(f"{", ".join(phone_list.keys())}\nEnter a name from the above name: ").title()
# Displaying the number corresponding to the name
print(phone_list.get(phone_name))