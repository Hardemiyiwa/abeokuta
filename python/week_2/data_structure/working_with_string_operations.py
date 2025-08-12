# Creating and manipulating strings
# upper()
name = "Ada Balogun"
print(name.upper())

# title()
sentence = "python is amazing"
print(sentence.title())

# strip
text = " Abuja "
print(text.strip())

# repace
message = "I love Java"
print(message.replace("Java", "Python"))

# swapcase
text = "Hello ABEOKUTA"
print(text.swapcase())

# lstrip
# Removes whitespace (or specifield characters) from the left side only.
text = " Nigeria"
print(text.lstrip())

# rstrip
# Removes whitespaces (or specified characters) from the right side only.
text = "Nigeria "
print(text.rstrip())

# split
# Splits a string into a list using a seperator (default is space).
fruits = "mango orange banana"
print(fruits.split())

# rsplit()
# Splits a string into a list from the right side.
text = "one,two,three,four"
print(text.rsplit(",",2))

# splitlines()
# Splits a string into a list at each newline (\n)
lines = "Lines 1\nLine 2\nLine 3"
print(lines.splitlines())

# join()
# Jins a list of strings into one string with a specified seperator.
words = ["I", "love", "Python"]
print(" ".join(words))

# center()
# Centers the string within a specified width, padding with spaces or characters.
text = "Python"
print(text.center(20, "-"))

# ljust()
# Left-aligns the string within a specified width, padding with spaces or characters
text = "Python"
print(text.ljust(10, "*"))

# rjust()
# Right-aligns the string within a specified width, padding with spaces or characters.
text = "Python"
print(text.rjust(10, "*"))

# zfill()
# Pads a numeric on the left with zeros until it reaches a given lenght.
num = "42"
print(num.zfill(5))

# isalpha()
# Checks if the string contains only letters
print("Lagos".isalpha()) # True
print("Lagos1234".isalpha()) # False

# isdigit()
# Checks if the string contains only digits.
print("12345".isdigit()) # True
print("123a".isdigit()) # false

# isalnum()
# Checks is the string contains only letters and digits.
print("Python3".isalnum())
print("Python 3".isalnum())