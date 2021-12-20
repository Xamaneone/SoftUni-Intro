n = int(input())

elements = set()


for _ in range(n):
    data = input()
    if " " in data:
        data = data.split(" ")
        for el in data:
            elements.add(el)
    else:
        elements.add(data)

for el in elements:
    print(el)