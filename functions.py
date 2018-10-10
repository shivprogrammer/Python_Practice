import os
cwd = os.getcwd()

students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def add_student(name, student_id=332):
    student = {"name": name, "student_id": student_id}
    students.append(student)


def save_file(student):
    try:
        f = open("students.txt", "a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print("Could not save file")


# What the fuck is going on, this commented out function doesn't work
# but the one right below it does???????
# def read_file():
#     try:
#         f = open("students.txt", "r")
#         for student in f.readLines():
#             add_student(student)
#         f.close()
#     except Exception:
#         print("Could not read file")


def read_file():
    try:
        f = open("students.txt", "r")
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print("Could not read file")


read_file()
print_students_titlecase()

student_name = input("Enter student name: ")
student_id = input("Enter student ID: ")

add_student(student_name, student_id)
save_file(student_name)

# user_wants_to_add_student = input("Would you like to add a student? (yes/no): ").lower()

# while user_wants_to_add_student == "yes":
#     name = input("Enter student name: ")
#     student_id = int(input("Enter student ID: "))
#     add_student(name, student_id)
#     print("")
#     user_wants_to_add_student = input("Would you like to add another student? (yes/no): ").lower()

