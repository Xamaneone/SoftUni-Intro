n = int(input())
names = []

for _ in range(n):
    names.append(input())


unique_names = set()

for name in names:
    unique_names.add(name)


for name in unique_names:
    print(name)