students = []


def read_file():
    try:
        f = open("students.txt", "r")
        for student in f.readLines():
            students.append(student)
        f.close()
    except Exception:
        print("Could not read file")


read_file()
print(students)