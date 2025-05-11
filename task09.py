student_marks={
    "Ajay":67,
    "Boby":99,
    "Chenu":78,
    "Dinesh":55,
    "Tushar":86
}

name=input("Enter the student's name: ")

if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found in the records.")
