first, second = input().split(" ")
total_sum = 0


if len(first) > len(second):
    cycle = len(second)
else:
    cycle = len(first)
for i in range(0, cycle):
    total_sum += ord(first[0]) * ord(second[0])
    first = first[1:]
    second = second[1:]

while len(first) != 0:
    for i in first:
        total_sum += ord(i)
        first = first[1:]
while len(second) != 0:
    for i in second:
        total_sum += ord(i)
        second = second[1:]

print(total_sum)