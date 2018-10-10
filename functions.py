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


user_wants_to_add_student = input("Would you like to add a student? (yes/no): ").lower()

while user_wants_to_add_student == "yes":
    name = input("Enter student name: ")
    student_id = int(input("Enter student ID: "))
    add_student(name, student_id)
    print("")
    user_wants_to_add_student = input("Would you like to add another student? (yes/no): ").lower()


print_students_titlecase()

# def get_students():
#     students = ["mark", "james"]
#
#     def get_students_titlecase():
#         students_titlecase = []
#         for student in students:
#             students_titlecase.append(student.title())
#         return students_titlecase
#     students_titlecase_names = get_students_titlecase()
#     print(students_titlecase_names)
#
#
# get_students()
