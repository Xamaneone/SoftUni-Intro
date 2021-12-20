act = int(input())
goal = 10000
steps = 0
while True:
    steps += act
    if steps >= goal:
        steps -= goal
        print(f"Goal reached! Good job!")
        print(f"{steps} steps over the goal!")
        break
    act = input()
    if act == "Going home":
        act = int(input())
        steps += act
        if steps >= goal:
            steps -= goal
            print(f"Goal reached! Good job!")
            print(f"{steps} steps over the goal!")
            break
        else:
            print (f"{goal - steps} more steps to reach goal.")
            break
    act = float(act)
    act = int(act)


