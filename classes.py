students = []


class Student:
    def __init__(self, name, student_id=332):
        self.name = name
        self.student = student_id
        students.append(self)

    def __str__(self):
        return "Student"

    def get_name_capitalize(selfs):
        return self.name.capitalize()


mark = Student("Mark")
print(mark)
