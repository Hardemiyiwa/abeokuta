# Attendance Tracker
# days of the weeks
days = ("Sunday", "Monday", "Tuesday", "wednesday", "Thursday", "Friday", "Saturday")
print(days[0])
# months of the years
months = ("January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

# Collecting student data
student_name = input("Enter your name: ").strip().title()
gender = input("Enter your gender: ").strip().title()
course_track = input("Enter your course track: ").title().strip()
Current_month = int(input("Enter your current month using(1 - 12): "))
current_day = int(input("Enter current day (1 - 7): "))

print(f"\n\nStudent name:\t\t{student_name}")
print(f"\nStudent gender:\t\t{gender}")
print(f"\nStudent course track:\t{course_track}")
print(f"\nmonth:\t\t\t{months[Current_month -1]}")
print(f"\nDay:\t\t\t{days[current_day - 1]}")