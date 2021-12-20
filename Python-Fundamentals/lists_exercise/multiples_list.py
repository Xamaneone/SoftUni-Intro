factor = int(input())
count = int(input())
numbers = []
for i in range(1, count + 1):
    num = factor * i
    numbers.append(num)
print(numbers)