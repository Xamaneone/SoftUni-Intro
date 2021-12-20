n = int(input())

first = 0
second = 0

for i in range(1, n + 1):
    neshto = int(input())
    if i  % 2 == 0:
        first += neshto
    else:
        second += neshto

if first == second:
    print("Yes")
    print (f"Sum = {first}")
else:
    diff = abs(first - second)
    print ("No")
    print (f"Diff = {diff}")