# Days and Activities Pairing
days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
# collecting user input for the selected days
print("Select three days of the weeks using (1 - 7)")
selected_days = [
    days[int(input("Enter the first day (1 - 7): ")) - 1],
    days[int(input("Enter the second day (1 - 7): ")) - 1],
    days[int(input("Enter the last day (1 - 7): ")) - 1]
]
print(selected_days)
# collecting user activities on each selected days
activities  = []
for i in range(len(selected_days)):
    user_activities = input(f"Enter your activity on {selected_days[i]}: ")
    activities.append(user_activities)
print(activities)
# storing it in a dictionary
day_activities = {day: activity for day, activity in zip(selected_days, activities)}
print(day_activities)
