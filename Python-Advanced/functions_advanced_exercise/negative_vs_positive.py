numbers = list(map(int, input().split()))

sum_of_positive = sum(filter(lambda num: num > 0, numbers))
sum_of_negative = sum(filter(lambda num: num < 0, numbers))

print(sum_of_negative)
print(sum_of_positive)

if abs(sum_of_negative) > sum_of_positive:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")