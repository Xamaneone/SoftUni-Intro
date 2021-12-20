counter = int(input())

students = {}
divide_by = {}
result = {}

for _ in range(counter):
    name = input()
    grade = float(input())
    if name not in students:
        students[name] = grade
        divide_by[name] = 1
    else:
        students[name] += grade
        divide_by[name] += 1

for student in students:
    grade = students[student] / divide_by[student]
    if grade >= 4.50:
        result[student] = grade

for student, av_grade in sorted(result.items(), key=lambda x: x[1], reverse=True):
    print(f"{student} -> {av_grade:.2f}")
