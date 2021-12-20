interval = int(input())
sum = 0
for num in range(1, interval + 1):
    symbol = input()
    sum += ord(symbol)
print(f"The sum equals: {sum}")