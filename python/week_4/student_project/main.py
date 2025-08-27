#  main.py - Project entry point

# main.py

import data
import utils

# Add some students
data.add_students("Paul", "AI Engineering")
data.add_students("Blessing", "AI Development")

# Print formatted student records
for s in data.get_students():
    print(utils.format_student(s))