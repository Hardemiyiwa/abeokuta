# Escape sequence in print - "\n", "\t"
print("Line1\nLine2")               # New line
print("Item1\tItem2")               # Tab space
print("He said, \"Hello\"")         # Quoted string
print('It\'s Python!')              #Apostrophe in single

# Newline (\n)
print("Welcome to python\nLet's learn together")

# Tab (\t)
print("Name\tAge\tLocation")
print("Aisha\t25\tLagos")

# Quotes inside string
print("She said, \"Hello there!\"")
print('It\'s a sunny day.')

# Backslash
print("File path: C:\\Users\\Aisha\\Documents")

# Carriage return (\r)
print("123456\rABC") # Output: ABC456 (replaces 123)

# Backspace (\b)
print("Helloo\b") # Output: Hello

# Bell/alert (may or may not deep depending on environment)
# print("\a") # Triggers a bell sound (if supported)

print("Hello\fworld")   # Form feed
print("Hello\vworld")   # Vertical tab

# Using sep and end in print
print("Python", "is", "fun", sep=" - ")
print("This is the first line.", end=" ")
print("This is the second line.")

# print("\t\t\t\t\t\t\t\t+\n\n\t\t\t\t\t\t\t+\t\t+\n\n\t\t\t\t\t\t+")
print("        +\n       +++\n      +++++\n     +++++++\n    +++++++++\n   +++++++++++")
print("        v\t\n       vvv\t\n      vvvvv\t\n     vvvvvvv\t\n    vvvvvvvvv\t\n   vvvvvvvvvvv\t\n  vvvvvvvvvvvvv\t\n vvvvvvvvvvvvvvv\t\nvvvvvvvvvvvvvvvvv\t\n")