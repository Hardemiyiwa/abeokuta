# list method
# 1. dot append() method
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits) # Output: ['apple', 'banana', 'cherry']

# 2. dot insert() method
# Inserts an element at a specific position
fruits = ["apple", "banana"]
fruits.insert(1, "orange")
print(fruits) # Output: ['apple', 'orange', 'banana']

# 3. dot extend() method
# Adds elements from another list (or iterable) to the end.
fruits = ["apple", "banana"]
tropical = ["mango", "pineapple"]
fruits.extend(tropical)
print(fruits) # ['apple', 'banana', 'mango', 'pineapple']

# 4. dot remove() method
fruits = ["apple", "banana", "cherry", "banana"]
fruits.remove("banana")
print(fruits) # Output: ['apple', 'cherry', 'banana']

# 5. dot pop() method
fruits = ["apple", "banana", "cherry"]
last_fruit = fruits.pop()
print(last_fruit)   # Output: cherry
print(fruits)       # Output: ['apple', 'banana']

# 6. dot clear() method
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits) # Output: []

# 7. dot index() method
fruits = ["apple", "banana", "cherry"]
position = fruits.index("banana")
print(position) # Output: 1

# 8. dot count() method
fruits = ["apple", "banana", "cherry", "banana"]
print(fruits.count("banana")) # Output: 2

# 9. dot sort() method
numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)  # [1, 2, 3, 4]

# descending order
numbers.sort(reverse=True)
print(numbers)  # [4, 3, 2, 1]

# 10. dot reverse() method
fruits = ["apple", "banana", "cherry"]
fruits.reverse()
print(fruits)   # Output: ['cherry', 'banana', 'apple']

# 11. copy()
fruits = ["apple", "banana", "cherry"]
new_list = fruits.copy()
print(new_list) # Output: ['apple', 'banana', 'cherry']