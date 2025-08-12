# List Operation in Python
# 1. Concatenation (+)
list1 = [1, 2, 3]
list2 = [4, 5]
result = list1 + list2
print(result) # [1, 2, 3, 4, 5]

# 2. Repetition (*)
nums = [1, 2]
repeated = nums * 3
print(repeated) # [1, 2, 1, 2, 1, 2]

#  3. Indexing
fruits = ["apple", "banana", "cherry"]
print(fruits[0])    # apple
print(fruits[-1])   # cherry (negative index starts from the end)

# 4. Slicing
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])     # [1, 2, 3]
print(numbers[:3])      # [0, 1, 2]
print(numbers[3:])      # [3, 4, 5]
print(numbers[::2])     # [0, 2, 4] (step of 2)

# 5. Membership (in / not in)
colors = ["red", "green", "blue"]
print("green" in colors)    # True
print("yellow" not in colors)   # True

# 6. Length (len())
items = ["pen", "book", "laptop"]
print(len(items))   # 3

# 7. Min and Max (min() / max())
nums = [5, 2, 9, 1]
print(min(nums))    # 1
print(max(nums))    # 9

# Sum (sum())
numbers = [1, 2, 3, 4]
print(sum(numbers)) # 10

# List Comprehension
squares = [x**2 for x in range(5)]
print(squares)

# Copying a List
a = [1 ,2 ,3]
b = a.copy() # or b = list(a)
print(b) # [1, 2, 3]