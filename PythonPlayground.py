# x = 0

# for index in range(10):
#     x += 10
#     print(f"The value of X is {x}")

student_names = ["James", "Katarina", "Jessica", "Mark", "Bort", "Frank Grimes", "Max Power"]

for name in student_names:
    if name == "Bort":
        continue
        print("Found him! " + name)
    print("Currently testing " + name)
