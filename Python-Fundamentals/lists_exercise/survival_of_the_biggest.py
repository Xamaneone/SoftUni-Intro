numbers = input().split(" ")
result = []
exterminate = int(input())
for num in numbers:
    temp = int(num)
    result.append(temp)
for i in range(0, exterminate):
    low_num = 9999
    for num in result:
        if num < low_num:
            low_num = num
    for index in range(0, len(result)):
        if result[index] == low_num:
            result.pop(index)
            break
print(result)