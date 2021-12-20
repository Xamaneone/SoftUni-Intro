from _collections import deque

container = deque()

name = input()
while name != "End":
    if name == "Paid":
        while container:
            print(container.popleft())
        name = input()
        continue
    container.append(name)
    name = input()

print(f"{len(container)} people remaining.")