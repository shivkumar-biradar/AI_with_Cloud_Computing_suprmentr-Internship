# Student Data Manager
students = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 90,
    "David": 66,
    "Eve": 78
}

topper = max(students, key=students.get)
average = sum(students.values()) / len(students)
grades = {name: ("A" if marks>=85 else "B" if marks>=70 else "C") for name, marks in students.items()}

print(f"Topper: {topper}")
print(f"Class Average: {average}")
print("Grades:", grades)
