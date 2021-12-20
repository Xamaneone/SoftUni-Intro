cycle = int(input())

left = 0
right = 0

for i in range(cycle):
    left += int(input())

for i in range(cycle):
    right += int(input())

if left == right:
    print(f"Yes, sum = {left}")
else:
    diff = abs(left-right)
    print (f"No, diff = {diff}")