n = int(input())
first = 0
second = 0
third = 0
four = 0
five = 0
for i in range(1, n + 1):
    number = int(input())
    if number < 200:
        first += 1
    elif 200 <= number <= 399:
        second += 1
    elif 400 <= number <= 599:
        third += 1
    elif 600 <= number <= 799:
        four += 1
    elif number >= 800:
        five += 1

first = first / n * 100
second = second / n * 100
third = third / n * 100
four = four / n * 100
five = five / n * 100

print (f"{first:.2f}%")
print (f"{second:.2f}%")
print (f"{third:.2f}%")
print (f"{four:.2f}%")
print (f"{five:.2f}%")

