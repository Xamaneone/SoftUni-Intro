points = 5364
goal = 8848
day = 1
state = {}
meters = 0
while True:
    state = input()
    if state == "Yes":
        day += 1
    if state == "END":
        print("Failed!")
        print(points)
        break
    if day == 6:
        print("Failed!")
        print(points)
        break
    meters = int(input())
    points += meters
    if points >= goal:
        print(f"Goal reached for {day} days!")
        break
