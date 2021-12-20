people = int(input())
capacity = int(input())
counter = 0
while True:
    people -= capacity
    counter += 1
    if people <= 0:
        break
print(counter)