# Sets in Python
# Creating Sets
# 1. Using curly braces
fruits = {"apple", "banana", "mango"}
print(fruits)

# 2. Using the set() constructor
numbers = set([1, 2, 3, 4])
print(numbers)

# 3. Creating an empty set (must use set(), not {})
empty_set = set()
print(empty_set)

# 4. From a string (duplicates removed automatically)
letters = set("mississippi")
print(letters)

# Characteristics of sets 
'''
1. Unordered: No defined indexing or sequence.
2. Unique elements: Duplicates are automatically removed.
3. Mutable: You can add or remove items.
4. Unindexed: You can't access elements using an index like my_set[0].
5. Supports mathematical set operation: Union, intersection, difference, symmetric differnce.
'''

# Set Operations
# a. Adding Element
colors = {"red", "blue"}
colors.add("green")
print(colors)

# b. Removing elements
colors.remove("blue") # Removes an element, raises error if not found
print(colors)
colors.discard("yellow") # Removes if found, no error if missing
print(colors)

# Pop an element
colors = {"red", "blue", "green"}
removed = colors.pop()
print("Removed:", removed)
print("Remaining", colors)

# Clear a Set
