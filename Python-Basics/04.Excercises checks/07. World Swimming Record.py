import math
record = float(input())
distance = float(input())
time = float(input())
slowdown = distance // 15 * 12.5
sum = distance * time
sum = sum + slowdown
if sum > record:
    sum -= record
    print(f"No, he failed! He was {sum:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {sum:.2f} seconds.")