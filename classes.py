students = []

class Student:
    def add_student(name, student_id=332):
        student = {"name": name, "student_id": student_id}
        students.append(student)


student = Student()

print(student)

new_student = Student()

print(new_student)