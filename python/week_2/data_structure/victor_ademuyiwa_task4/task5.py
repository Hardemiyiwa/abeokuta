# Student Score Tracker
# asking user for user for the student name and score
student_names = input("Enter 3 student name (seperated by space): ").split(" ")
student_score = []
student_score.append(int(input(f"Enter {student_names[0]} score: ")))
student_score.append(int(input(f"Enter {student_names[1]} score: ")))
student_score.append(int(input(f"Enter {student_names[-1]} score: ")))
# printing the output
print(f"\n\tName\t\tScore\n\t{student_names[0]}\t\t{student_score[1]}\n\t{student_names[1]}\t\t{student_score[0]}\n\t{student_names[-1]}\t\t{student_score[-1]}")
