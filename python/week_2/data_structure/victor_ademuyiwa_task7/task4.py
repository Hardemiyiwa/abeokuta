# Unique Members Registration
# collecting user input
user = input("Enter three names \"seperated by comma\": ").split(",")
unique_members = set(user)
# creating dictionary
names_length = {name: len(name) for name in unique_members}
print(names_length)