from _collections import deque

cups = deque(input().split(" "))
bottles = deque(input().split(" "))

wasted_water = 0

current_cup = 0

while True:
    if not cups:
        print(f"Bottles: {' '.join(bottles)}")
        print(f"Wasted litters of water: {wasted_water}")
        break
    elif not bottles:
        print(f"Cups: {' '.join(cups)}")
        print(f"Wasted litters of water: {wasted_water}")
        break

    current_bottle = int(bottles.pop())
    if current_cup == 0:
        current_cup = int(cups.popleft())

    current_cup -= current_bottle

    if current_cup < 0:
        wasted_water += abs(current_cup)
        current_cup = 0