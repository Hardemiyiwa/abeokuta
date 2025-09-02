# Classes
class Student:
    def __init__(self, name, course, level):
        print("Creating a new student...")
        self.name = name
        self.course = course
        self.level = level
        print(f"Student {name} has been created!")

Student("ade", "ai_eng", 300)

# When you create a student, __init__ runs automatically
kemi = Student("Kemi Adebayo", "Computer Science", 300)

"""
**Visual Illustration**
Class: Student (The Template)
├── def __init__(self, name, course):
│   ├── self.name = name      ← "Give THIS object a name"
│   └── self.course = course  ← "Give THIS object a course"

Creating Objects:
├── kemi = Student("Kemi", "CS")
│   └── self refers to kemi → kemi.name = "Kemi"
├── chinedu = Student("Chinedu", "Engineering") 
│   └── self refers to chinedu → chinedu.name = "Chinedu"
└── fatima = Student("Fatima", "Medicine")
    └── self refers to fatima → fatima.name = "Fatima"
"""

# How init and self work together

class NigeriaStudent:
    def __init__(self, name, state, course):
        print(f"Step 1: Creating student object...")
        self.name = name                # Step 2: Assign name to THIS object
        self.state_of_origin = state    # Step 3: Assign state to THIS object
        self.course = course            # Step 4: Assign course to THIS object
        self.student_id = self.generate_id()    # Step 5: Generate ID for THIS object
        print(f"Step 6: {self.name} from {self.state_of_origin} is ready!")

    def generate_id(self):
        import random
        return f"UNISAIL{random.randint(1000, 9999)}"
    
# When you create a object an object, here's what happens:
ayo = NigeriaStudent("Ayo Daniel", "Lagos", "Street Statistics")

print(ayo.name)
print(ayo.student_id)

class PhoneUser:
    def __init__(self, name, network):
        self.name = name
        self.network = network
        self.airtime = 0
        print(f"{self.name} joined {self.network} network")

    def buy_airtime(self, amount):
        self.airtime += amount # self ensures it goes to the Right person
        return f"{self.name} now has ₦{self.airtime} airtime"

# Creating multiple users
abeeb = PhoneUser("Abeeb Bakare", "MTN")
onisemo = PhoneUser("Onisemo Williams", "Airtel")

# Each person's actions affect only their own account
print(abeeb.buy_airtime(500))       # Abeeb now has ₦500 airtime
print(onisemo.buy_airtime(1000))    # Onisemo now has ₦1000 airtime
print(abeeb.airtime)                # 500 (Abeeb's airtime unchanged)
print(onisemo.airtime)              # 1000 (Onisemo's airtime unchange)

# Defining Attributes of a student
class Student:
    def __init__(self, name, course, level, state_of_origin):
        self.name = name
        self.course = course
        self.level = level
        self.state_of_origin = state_of_origin
        self.cgpa = 0.0

# Creating a student object
Fathia = Student("Fathia Abdul", "Biochemistry", 300, "Ogun State")

# Acceing attribute
print(Fathia.name)
print(Fathia.course)
print(Fathia.state_of_origin)

# Type of Attribute
# 1. Instance Attributes - Unique to each object

student1 = Student("Antony Johnson", "Engineering", 200, "Ogun")
student2 = Student("Fadilat Hassan", "Medicine", 400, "Lagos")

print(student1.name)
print(student2.name)

# 2. Class Attributes - Shared by all objects of the class

class Student:
    university = "Federal University of Thechnology Akure"

    def __init__(self, name, course):
        self.name = name
        self.course = course



student1 = Student("Antony Johnson", "Engineering")
student2 = Student("Fadilat Hassan", "Medicine")

print(Student.university)
print(student1.university)
print(student2.university)

# Methods: The Actions (What Object CAN DO)

class Student:
    def __init__(self, name, course, level):
        # Attributes
        self.name = name
        self.course = course
        self.level = level
        self.cgpa = 0.0
        self.fee_paid = False

    # Mthod: action the student can do
    def pay_school_fees(self):
        self.fees_paid = True
        return f"{self.name} has registered courses for {self.level} level"
    
    # Method: another action
    def register_courses(self):
        if self.fees_paid:
            return f"{self.name} has registered courses for {self.course}"
        else:
            return f"{self.name} must pay school fees first!"
        
        # Method: calculates CGPA
    def calculate_cgpa(self, grades):
        if grades:
            self.cgpa = sum(grades) / len(grades)
            return f"{self.name}'s CGPA is now {self.cgpa:.2f}"
        return "No grades provided"
    
# Using methods
Abiodun = Student("Abiodun Akinola", "Gistology", 600)
print(Abiodun.pay_school_fees())
print(Abiodun.calculate_cgpa([4.2, 3.8, 4.0, 3.5]))

# Types of Methods
# 1. Instance Methods - Work with specific object data

#  self refers to the specific student
def pay_school_fees(self):
    return f"{self.name} has paid school fees"

# 2. Class Methods - Work with class-level data
@classmethod
def get_university(cls):
    return cls.university

# 3. Static methods - Don't need object or class data
# @stasticmethod
# def academic_Calendar():
#     return "Academic session runs from September to July"

# How Attributes and Methods Work Together
"""
# The Relationship
    - Attributes store the data
    - Methods use and modify that data
"""

class BankAccount:
    def __init__(self, owner, bank_name, balance = 0):
        # Attributes - What the account HAS
        self.owner = owner
        self.bank_name = bank_name
        self.balance = balance
        self.account_number = self.generate_account_number()

    # METHODS - What the account can do
    def deposit(self, amount):
        """Add money to the account"""
        if amount > 0:
            self.balance += amount # Method changes attribute
            return f"₦{amount:,} deposited to {self.owner}'s {self.bank_name} acount. New balance: ₦{self.balance}"
    
    def withdraw(self, amount):
        """Remove money from account"""
        if amount > 0 and amount < self.balance:
            self.balance -= amount
            return f"{amount:,} withdraw from {self.owner}'s account. New balance: ₦{self.balance:,}"
        return "Insufficient funds or invalid amount"
    
    def transfer(self, amount, recipient):
        """transfer money to another account"""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"₦{amount:,} transferred from {self.owner} to {recipient}. Remaining balance: ₦{self.balance:,}"
        return "Transfer failed: Insufficient funds"
    
    def check_balance(self):
        """Check current balance"""
        return f"{self.owner}'s {self.bank_name} acoont balance: ₦{self.balance:,}"
    
    def generate_account_number(self):
        """Generate a unique account number"""
        import random
        return f"01{random.randint(10000000, 99999999)}"
    
# Creating and using the account
adunni_account = BankAccount("Adunni Olaleye", "AXT Bank", 50000)

# Attributes (characteristics)
print(f"Owner: {adunni_account.owner}")
print(f"Bank: {adunni_account.bank_name}")
print(f"Account Number: {adunni_account.account_number}")