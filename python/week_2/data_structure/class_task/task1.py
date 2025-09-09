# Display user input to uppercase
display_uppercase = input("Enter ur name: ").upper()
print(display_uppercase)

# printing the first and the last letter
word = "python"
print(word[0],word[-1])

name = input("What is your name? ")
print("Hello, ! where is the user's input")

# character count
count = input("Mary has a little lamp\nEnter the character u want count from the sentence above: ")
print(f"\"{count}\" appear {"Mary has a little lamp".count(count)} times")

# Replacing World with python
word = "Hello World"
print(word.replace("World", "Python"))