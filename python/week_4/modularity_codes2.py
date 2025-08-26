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
