cycle = int(input())
result = []
for i in range(cycle):
    result.append(int(input()))
act = input()

if act == "even":
    for i in range(cycle - 1 , -1, -1):
        if result[i] % 2 != 0:
            result.pop(i)

if act == "odd":
    for i in range(cycle - 1 , -1, -1):
        if result[i] % 2 != 1:
            result.pop(i)

if act == "positive":
    for i in range(cycle - 1 , -1, -1):
        if result[i] < 0:
            result.pop(i)

if act == "negative":
    for i in range(cycle - 1 , -1, -1):
        if result[i] > -1:
            result.pop(i)


print(result)
