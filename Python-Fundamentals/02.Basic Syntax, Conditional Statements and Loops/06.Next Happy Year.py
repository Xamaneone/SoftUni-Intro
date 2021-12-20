year = int(input())

year += 1

while True:
    if len(str(year)) == len(set(str(year))):
        break
    else:
        year += 1

print(year)
