def add_student(students, name, grade):
    # Check if the student already exists
    for student in students:
        if student[0] == name:
            print(f"Student {name} already exists.")
            return
    # Add the new student
    students.append((name, grade))
    print(f"Student {name} added with grade {grade}.")

# Example usage
students = []
add_student(students, "Alice", 85)
print(students)  # Should print: [('Alice', 85)]
