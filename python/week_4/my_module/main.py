# my_module/main.py

import first
import second

# lets use the functions in the first.py file

print("=== math Function ===")
print("5 + 3 =", first.add(5, 3))
print("10 - 4 =", first.subtract(10, 4))
print("6 * 7 =", first.multiply(6, 7))
print("20 / 5 =", first.divide(20, 5))

# Lets use the functions in the second.py file
print("\n=== String Function ===")
print("\n=== String Function ===")
print(second.greet("Ridwan"))
print("Reverse of 'Python' =", second.reverse_string("Python"))
print("Character count in sentence =", second.count_characters("Python modules are powerful"))
print("Word count in sentence =", second.count_words("python modules are powerful"))