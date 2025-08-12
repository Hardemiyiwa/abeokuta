# Method 1: Using square brackets
empty_list = []
print(empty_list) # Output: []

# Method 2: Using the list() constructor
empty_list2 = list()
print(empty_list2) # Output: []

# List of integers
numbers = [1, 2, 3, 4, 5]
print(numbers) # Output: [1, 2, 3, 4, 5]

# List of strings
fruits = ["apple", "banana", "cherry"]
print(fruits) # output: ["apple", "banana", "cherry"]

# Mixed data types
mixed_list = ["Alice", 25, 5.8, True]
print(mixed_list) # output: ["Alice", 25, 5.8, True]

# From a string (each character becomes an element)
chars = list("hello")
print(chars) # Output: ['h', 'e', 'l', 'l', 'o']

# From a tuple
my_tuple = (10,20,30)
list_from_tuple = list(my_tuple) 
print(list_from_tuple) #Output [10, 20, 30]

# From a range
numbers_range = list(range(5))
print(numbers_range) # Output: [0, 1, 2, 3, 4]

# Square of numbers 0-4
squares = [x**2 for x in range(5)]
print(squares) # Output: [0, 1, 4, 9, 16]

# Even numbers between 0-10
evens = [x for x in range(11) if x % 2 == 0]
print(evens) # Output: [0, 2, 4, 6, 8, 10]

# Odds numbers between 0 - 10
odds = [x for x in range(11) if x % 2 != 0]
print(odds)

# Matrix-like list
matrix = [[1, 2], [3, 4], [5, 6]]
print(matrix) # [[1, 2], [3, 4], [5, 6]]

# Accessing elements in a nested list
print(matrix[0]) # Output: [1, 2]
print(matrix[0][1]) # Output: 2

# Characteristics of a list
# 1. Ordered collection
fruits = ["mango", "orange", "banana"]
print(fruits)       # ["mango", "orange", "banana"]
print(fruits[0])    # mango (first statement)
print(fruits[2])    # banana (third statement)

# 2, Allows Duplicates
items = ["rice", "beans", "yam", "rice"]
print(items) # Output: ["rice", "beans", "yam", "rice"]

# 3. Mutable (Can be change)
numbers = [1, 2, 3]
numbers[1] = 20 # Changing element at index 1
print(numbers)  # [1, 20, 3]

# 4. Can contain Different Data types
mixed = [10, "Nigeria", 3.14, True]
print(mixed)    # Output: [10, "Nigeria", 3.14, True]

# 5. Can be Nexted
nested_list = [[1, 2], ["a", "b"]]
print(nested_list)          # [[1, 2], ['a', 'b']]
print(nested_list[0][1])    # 2

# 6. Dynamic size
names = ["Ada"]
names.append("Bola")
names.append("Chidi")
print(names) # ['Ada', 'Bola', 'Chidi']
