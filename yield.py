students = []


def read_file():
    try:
        f = open("students.txt", "r")
        for student in f.readlines(): # for fucks sake please NEVER GOD DAMN CAPITALIZE LINES AGAIN GOD DAMN IT
            students.append(student)
        f.close()
    except Exception:
        print("Could not read file")


read_file()
print(students)
