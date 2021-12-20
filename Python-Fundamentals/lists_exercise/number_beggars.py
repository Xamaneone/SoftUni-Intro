numbers = input().split(", ")
beggars = int(input())
result = []
for beggar in range(0, beggars):
    num = 0
    for i in range(beggar, len(numbers), beggars):
        num += int(numbers[i])
    result.append(num)
print(result)
