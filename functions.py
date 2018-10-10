students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase = student.title()
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def add_student(name, student_id=332):
    student = {"name": name, "student_id": student_id}
    students.append(student)


def var_args(name, *args):
    print(name)
    print(args)


student_list = get_students_titlecase()

add_student(name="Mark", student_id=15)

var_args("Mark", "Loves Python", None, "Hello", True)
