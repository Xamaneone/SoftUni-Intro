data = input().split(".")
version = [int(num) for num in data]
version[2] += 1
if version[2] == 10:
    version[1] += 1
    version.pop(2)
    version.append(0)
    if version[1] == 10:
        version[0] += 1
        temp = version[2]
        version.pop(1)
        version.pop(1)
        version.append(0)
        version.append(temp)
print(f"{version[0]}.{version[1]}.{version[2]}")