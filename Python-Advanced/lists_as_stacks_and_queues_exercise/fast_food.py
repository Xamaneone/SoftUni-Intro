from _collections import deque

food_storage = int(input())
queue = deque()

orders = input().split(" ")
for order in orders:
    queue.append(int(order))

max_order = max(queue)
print(max_order)


pop = 0
for order in queue:
    if food_storage >= order:
        pop += 1
        food_storage -= order
    else:
        break


counter = 0
while counter != pop:
    counter += 1
    queue.popleft()



if len(queue) == 0:
    print("Orders complete")
else:
    result = ""
    for order in queue:
        result += f" {str(order)}"
    print(f"Orders left:{result}")