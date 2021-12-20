result = {}

resource = input()
while resource != "stop":
    quantity = int(input())
    if resource in result:
        result[resource] += quantity
        resource = input()
        continue
    else:
        result[resource] = quantity
        resource = input()

for resource, quantity in result.items():
    print(f"{resource} -> {quantity}")