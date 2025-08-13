# Creating Tuples
# 1. Using parentheses ()
# Example 1: tuple with multiple
fruits = ("apple", "banana", "cherry")
print(fruits) # ('apple', 'banana', 'cherry')

# 2. Without parentheses (tuple packing)
numbers = 1, 2, 3
print(numbers) # (1, 2, 3)

# 3. Single-item tuple (must include a comma)
single_item = ("apple",)
print(single_item)      # ('apple',)
print(type(single_item)) # <class 'tuple'>

#  4. Using the tuple() constructor
fruits_list = ["apple", "banana", "Cherry"]
fruits_tuple = tuple(fruits_list)
print(fruits_tuple) #   ('apple', 'banana', 'cherry')

# Characteristics of Tuples
# 1. Ordered - Items have a fixed position
colors = ("red", "green", "blue")
print(colors[0])    # red

# 2. Immutable - Cannot change after creation (uncomment and run. This will cause an error)
# colors[1] = "yellow" # TypeError

# 3. Allow duplicates
numbers = (1, 2, 2, 3)
print(numbers)  # (1, 2, 2, 3)

# 4. Mixed data types
mixed = ("apple", 3, True, 5.6)
print(mixed)    # ('apple', 3, True, 5.6)

# 5. Nested tuples
nested = (("a", "b"), (1, 2))
print(nested) # (('a', 'b'), (1, 2))

# Tuple Operations
# 1. Indexing
fruits = ("apple", "banana", "cherry")
print(fruits[1])    # banana
print(fruits[-1])   # cherry

# 2. concatenation
tuple1 = (1, 2)
tuple2 = (3, 4)
result = tuple1 + tuple2
print(result)   # (1, 2, 3, 4)

# 3. Slicing
print(fruits[0:2])  # ('apple', 'banana')
print(fruits[::-1]) # ('cherry', 'banana', 'apple')

# 4. Repetition
nums = (1, 2)
print(nums * 3)

# 5. Membership
fruits = ("apple", "banana", "cherry")
print("banana" in fruits)   # True
print("grape" not in fruits) # True

# 6. Iteration
for fruit in fruits:
    print(fruit)

# Unpacking Tuples
person = ("John", 25, "Nigeria")
name, age, country = person 
print(name) # John
print(age) # age
print(country) # Nigeria

# Tuple Methods - it only have two method
# dot count() and dot index()

numbers = (1, 2, 2, 3, 4)

print(numbers.count(2)) # 2 (counts occurences of 2)
print(numbers.index(3)) # 3 (position of the first occurrence of 3)

# Converting Between list and Tuple
# Tuple to list
t = (1, 2, 3)
lst = list(t)
lst.append(4)
print(lst) # [1, 2, 3, 4]

# List back to Tuple
t = tuple(lst)
print(t) # (1, 2, 3, 4)

# Built-in Function with Tuples
nums = (4, 1, 7, 3)

print(len(nums))    # 4
print(max(nums))    # 7
print(min(nums))    # 1
print(sum(nums))    # 15