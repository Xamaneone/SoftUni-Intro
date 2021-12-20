raters = int(input())
sum = 0
all = 0
counter = 0
name_of_presentation = str(input())
while name_of_presentation != "Finish":
    for i in range(1, raters+1):
        grade = float(input())
        sum += grade
        all += grade
    sum = sum / raters
    print (f"{name_of_presentation} - {sum:.2f}.")
    counter += 1
    sum = 0
    name_of_presentation = str(input())
print (f"Student's final assessment is {all / (counter*raters):.2f}.")






