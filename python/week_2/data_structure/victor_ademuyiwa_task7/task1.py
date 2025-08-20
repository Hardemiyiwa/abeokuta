# Student Bio Data Storage
student = {}
# Collecting student data
name = input("Enter your name: ").title().strip()
age = int(input("Enter your age: "))
gender = input("Enter your gender: ").title().strip()
courses = input("Enter your course list \"seperated by space\": ").title().split()

student.update({"name": name, "age": age, "gender": gender, "courses": courses})

print("\n---- Student Bio Data ----")
print(f"Name\t\t{student.get("name")}\nAge\t\t{student["age"]}\nGender\t\t{student["gender"]}\nCourses\t\t{", ".join(student["courses"])}")