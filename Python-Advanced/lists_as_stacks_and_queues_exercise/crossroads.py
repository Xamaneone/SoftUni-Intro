from _collections import deque

green_light = int(input())
free_window = int(input())
cars = deque()
crash = False
passed = 0


x = str(input())

while x != "END":
    current_car = 0
    current_car_name = ""
    crash_chr = 0
    if x == "green":
        for s in range(green_light):
            if cars:
                if current_car < 1:
                    car = cars.popleft()
                    current_car = len(car)
                    current_car_name = car
                    passed += 1
                    crash_chr = 0
            current_car -= 1
            crash_chr += 1
        for s in range(free_window):
            current_car -= 1
            crash_chr += 1
    else:
        cars.append(x)
    if current_car > 0:
        crash = True
        print("A crash happened!")
        print(f"{current_car_name} was hit at {current_car_name[crash_chr]}.")
        break




    x = str(input())

if not crash:
    print(f"Everyone is safe.")
    print(f"{passed} total cars passed the crossroads.")