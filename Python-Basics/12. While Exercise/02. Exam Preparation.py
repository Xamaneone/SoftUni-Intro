worst_grade = int(input())
worst_counter = 0
exam_counter = 0
exam_grade = 0
last_problem = {}
while worst_counter != worst_grade:
    name = input()
    if name == "Enough":
        print (f"Average score: {exam_grade / exam_counter:.2f}")
        print (f"Number of problems: {exam_counter}")
        print (f"Last problem: {last_problem}")
        break
    last_problem = name
    grade = float(input())
    exam_counter += 1
    exam_grade += grade
    if grade <= 4:
        worst_counter += 1

if worst_counter == worst_grade:
    print (f"You need a break, {exam_counter - 1} poor grades.")
