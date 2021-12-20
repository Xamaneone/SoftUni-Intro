age = float(input())
gender = input()
if gender == "m":
    if age < 16:
        print ("Master")
    else:
        print ("Mr.")

if gender == "f":
    if age < 16:
        print ("Miss")
    else:
        print ("Ms.")