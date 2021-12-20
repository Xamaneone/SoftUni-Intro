command = str(input())

numbers = list(map(int, input().split()))


if command == "Odd":
    print((sum(filter(lambda num: num % 2 == 1, numbers))) * len(numbers))
elif command == "Even":
    print((sum(filter(lambda num: num % 2 == 0, numbers))) * len(numbers))