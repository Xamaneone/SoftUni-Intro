courses = {}

data = input()

while not data == "end":
    course, student = data.split(" : ")
    if course not in courses:
        courses[course] = [student]
    else:
        courses[course].append(student)

    data = input()


for course, students in sorted(courses.items(), key=lambda x: -len(x[1])):
    print(f"{course}: {len(students)}")
    for student in sorted(students):
        print(f"-- {student}")