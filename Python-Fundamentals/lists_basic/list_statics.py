positive = []
negative = []
sum = 0
numbers = int(input())
for i in range(0, numbers):
    num = int(input())
    if num >= 0:
        positive.append(num)
    else:
        negative.append(num)

for num in negative:
    sum += num
print(positive)
print(negative)
print(f"Count of positives: {len(positive)}. Sum of negatives: {sum}")