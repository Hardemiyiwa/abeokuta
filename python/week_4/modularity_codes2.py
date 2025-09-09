# Python Modules
# 1. Import the whole module

import math

# Lets put it to use

print(math.sqrt(9))
#  - Note that you must specify the module name when calling a function within it.

# 2. import as an alias
import math as m

# lets put it to use

print(m.sqrt(25))
# - This shortens the module name, this is common with libraries like numpy, pandas, etc

# 3. Import specific functions or variables

from math import sqrt, pi

print(sqrt(36))
print(pi)
# - here you don't need the prefix 'math.' anymore

# 4. Import everything from the module

from math import *

print(sqrt(49))
print(pi)

# - this is usually not recommended because it can cause name conflits if two modules have functions with the same name

"""
Writing Your Own Module
- step1: Create a folder. Name it my_module
- step2: Create a file inside the folder. Name it first.py
- step3: create another file inside the same folder. name it second.py
- step4: create another file still inside the same folder. Name it main.py
"""

# 4. Python Packages
"""
what is a package?
- A package in python is a way to organize related modules together into a folder.
- inside this folder, there must be a special file called __init__.py(can be empty). this file tells python that the folder should be treated as a package.
- hmmm, let think of a package as a standard mechanic workshop, and each module is a different toolbox inside he workshop. The init.py file is like the label on the workshop telling passerbys that this is a mechanic workshop.
"""

# Third-Party packages
"""
Python comes with some built-in modules, but you can also install extra packages created by others.
These packages are stored in the Python Package Index (PyPi).
We install them using pip (Python's package manager) or conda a
"""

# Creating your Package
# my_project/
# │
# ├── my_package/              # Package folder
# │   ├── __init__.py          # Makes this folder a package
# │   ├── math_utils.py        # Module 1
# │   ├── string_utils.py      # Module 2
# │
# └── main.py                  # Script that uses the package

# 5. Code Reusability
"""
What is code Reusability?
- Code reusability means writing code once and using it multiple times instead of rewriting it.
- It helps to make programs cleaner, faster to develop, and easier to maintain.
- In python, code reusability is achieved using:
    - Functions(reusing blocks of code)
    - modules (saving functions in .py files to import later)
    - Packages (organizing modules in folders)
    - Classes & Objects(OOP makes reusable blueprints)
    - Libraries (built-in or third-party)
"""
"""
Why reuse code?
- Saves time - no need to rewrite the same logic.
- Avoids duplication - reduces errors from copy and paste.
- Improves readability - your code is modular and organized.
- Easy to maintain - update once, reuse everywhere.
"""

# 6. Organizing a Python Project
"""
- A modular project is a way of organizing your code into seperate files and folders, each responsible for a specific task.
- this makes the project easier to read, test, and maintain.
"""

"""
Why Use Modular Structure?
- seperates concerns - Each file has one responsibility.
- Easier to debug - You can fix issues in one place without breaking others.
- Reusability - Functions/modules can be reused in other projects.
- Collaboration-friendly - Multiple developers can work on different parts.
"""
"""
- Let's say we want to build a Student Records Projects.
- We will first structure our folder and files like this.
student_project/
│
├── data.py        # Handles storing and retrieving student data
├── utils.py       # Contains helper functions (e.g., calculations, formatting)
├── main.py        # Entry point to run the project
"""

"""
Let's try A Bigger Project Structure
    - As the project grow, we can organize into folder

Lets work on Library Management System
    - The goal of this project is to
    - Manage books in a library
    - Add books, list books, and borrow books.
    - Organized into folders and files for modularity.

Lets structue the folder and possible files
library_project/
│
├── my_data/                   # Handles storage & retrieval
│   ├── __init__.py
│   └── data.py
│
├── utils/                  # Helper functions
│   ├── __init__.py
│   └── helpers.py
│
├── services/               # Core business logic
│   ├── __init__.py
│   └── library.py
│
├── main.py                 # Entry point of the program
└── requirements.txt        # (optional) external dependencies
"""

"""
Lets make the scope of the implementation broader and broader and interactive
    - Lets have our project structure

library_project/
│
├── my_data/
│   └── data.py
│
├── utils/
│   └── helpers.py
│
├── services/
│   └── library.py
│
└── main.py
"""
