name = input()
sum = float(0)
grade = float(input())
count = 0
while count != 13:
    grade = float(grade)
    count += 1
    grade = round(grade, 2)
    sum += grade
    round(sum, 2)
    if grade == 2:
        print (f"{name} has been excluded at {count} grade")
        break
    grade = float(grade)
    grade = int(grade)
    if grade >= 4:
        if count == 12:
            break
        grade = input()
    else:
        print (f"{name} has been excluded at {count} grade")
        break
grade = sum / 12
if grade >= 4 and count == 12:
    print (f"{name} graduated. Average grade: {grade:.2f}")