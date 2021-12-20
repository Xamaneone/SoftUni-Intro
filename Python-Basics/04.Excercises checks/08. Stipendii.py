import math
income = float(input())
average = float(input())
min_icnome = float(input())

excelent = float(0)
social = float(0)

if income < min_icnome :
    social = 0.35 * min_icnome

if average > 5.50 :
    excelent = average * 25

if excelent + social == 0:
    print ("You cannot get a scholarship!")
if excelent + social != 0:
    if social > excelent:
        print (f"You get a Social scholarship {math.floor(social)} BGN")
    if excelent >= social:
        print (f"You get a scholarship for excellent results {math.floor(excelent)} BGN")






