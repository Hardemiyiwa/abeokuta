# Single quote
name = 'Ada'
print(name)

# Double quotes
greeting = "Hello"
print(greeting)

# Triple quotes (for multi-line strings)
story = '''Once upon a time,
there was a coder named Ada.'''
print(story)

# String with numbers and symbols
password = "p@ssw0rd123"
print(password)

# Indexing
word = "Welcome to Python programming language"
print(word[0]) # W
print(word[-1]) # e

# Slicing
print(word[0:4]) # Welc
print(word[2:]) # lcome to python programing language
print(word[:3]) # Wel
print(word[::2]) # Wloet yhnpormiglnug
print(word[::-1])
print("python"[::-1])

# Sting Concatenation & repitition
# concatenation
a = "Hello"
b = "World"
print(a + " " + b) # Hello world

# Repetition
word = "Hi "
print(word * 3) # Hi! H! H!

# String Searching & Checking
# Membership
text = "Python programming"
print("Python" in text) # True
print("Java" not in text) # True

# index() / rindex()
# (like find() but raises an error if not found)
text = "Hello World"
print(text.index("world")) # 6

# find() / rfind()
text = "Hello World"
print(text.find("o")) # 4
print(text.rfind("o")) # 7

# startswith() / endswith()
filename = "data.csv"
print(filename.startswith("data")) # True
print(filename.endswith(".csv")) # True