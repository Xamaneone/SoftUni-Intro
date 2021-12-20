import sys
max_num = -sys.maxsize
sum_numbers = 0
numbers = int(input())
for i in range(0, numbers):
    num = int(input())
    if num > max_num:
        max_num = num

    sum_numbers += num

sum_numbers -= max_num
if max_num == sum_numbers:
    print("Yes")
    print(f"Sum = {sum_numbers}")
else:
    print("No")
    sum_numbers -= max_num
    print(f"Diff = {abs(sum_numbers)}")