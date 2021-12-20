from _collections import deque

box = deque(input().split(" "))

rack_capacity = int(input())

racks = 0
capacity = 0
while len(box) != 0:
    dress = int(box.pop())
    if dress != 0 and capacity == 0:
        racks += 1
    if capacity + dress > rack_capacity:
        racks += 1
        capacity = 0
        capacity += dress
        continue
    capacity += dress

print(racks)
