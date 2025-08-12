# Name Organizer
names = input("Enter five (5) \"seprate each name with space\" :")
# lower case converter
name_to_lower = names.lower()
# convert names to list
name_list = name_to_lower.split(" ")
name_list.sort()
print(name_list)
for name in range(len(name_list)):
    print(name_list[name])