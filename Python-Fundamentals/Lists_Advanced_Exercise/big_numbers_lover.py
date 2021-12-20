numbers = input().split(" ")
numbers.sort(reverse=True)
for num in numbers:
    print(num, end="")
