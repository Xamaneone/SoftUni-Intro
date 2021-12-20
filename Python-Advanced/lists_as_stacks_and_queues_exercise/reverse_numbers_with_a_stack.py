from _collections import deque

integers = deque(input().split(" "))
result = deque()
while integers:
    result.append((integers.pop()))

for num in result:
    print(num, end=" ")