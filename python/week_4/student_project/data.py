# data.py
students = []

def add_students(name, track):
    students.append({"name": name, "track": track})

def get_students():
    return students