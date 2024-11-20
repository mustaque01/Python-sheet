def second_lowest_students(records):
    # Sort the list by grades (second element in each sub-list)
    sorted_records = sorted(records, key=lambda x: x[1])
    
    # Find the second lowest grade
    lowest_grade = sorted_records[0][1]
    second_lowest_grade = None
    for name, grade in sorted_records:
        if grade > lowest_grade:
            second_lowest_grade = grade
            break

    # Collect names of students with the second lowest grade
    second_lowest_students = [name for name, grade in sorted_records if grade == second_lowest_grade]
    
    # Sort names alphabetically
    second_lowest_students.sort()
    
    # Print names
    for student in second_lowest_students:
        print(student)

# Example usage
students = [
    ["Harry", 37.21],
    ["Berry", 37.21],
    ["Tina", 37.2],
    ["Akriti", 41],
    ["Harsh", 39],
]

second_lowest_students(students)
