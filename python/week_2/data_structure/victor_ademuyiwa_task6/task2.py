#  Unique Name
# creating an empty list
seminal_attendance = set()
# collecting the estimated total number of people attending the seminar
total_estimated_number = int(input("Enter the estimated total number people attending the program: "))
# Adding the collected to the set
for attendance in range(total_estimated_number):
    attendance = input("Enter your name (Enter done when there is no member left): ")
    if attendance.lower().strip() == "done":
        break
    else:
        seminal_attendance.add(attendance)
# displaying the name in alphabetical order
print(f"{", ".join(sorted(seminal_attendance))}")