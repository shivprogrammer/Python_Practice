students = []

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase = student.title()
    return students_titlecase

def print_students_titlecase():
    students_titlecase = []
    for student in students:
        student_titlecase = student.title()
    print(students_titlecase)

def add_student(name):
    students.append(name)

student_list = get_students_titlecase()