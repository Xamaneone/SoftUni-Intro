def positive_or_negative_num(number):
    if number < 0:
        negative.append(str(number))
        return
    positive.append(str(number))
    return

def odd_or_even_num(number):
    if number % 2 == 0 or number == 0:
        even.append(str(number))
        return
    odd.append(str(number))
    return


numbers = list(map(int, input().split(", ")))

positive = []
negative = []
even = []
odd = []

[positive_or_negative_num(num) for num in numbers]
[odd_or_even_num(num) for num in numbers]

print(f"Positive: {', '.join(positive)}")
print(f"Negative: {', '.join(negative)}")
print(f"Even: {', '.join(even)}")
print(f"Odd: {', '.join(odd)}")