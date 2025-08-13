# Tuple Unpacking
# collecting users data
user_first_name = input("Enter your first name: ")
user_age = input("Enter your age name: ")
user_favorite_color = input("Enter your Favorite color: ")
user_home_town = input("Enter Home town name: ")

user_data = (user_first_name, user_age, user_favorite_color, user_home_town)

# Unpacking into variable
first_name, age, favorite_color, home_town = user_data
print(first_name)
print(age)
print(favorite_color)
print(home_town)