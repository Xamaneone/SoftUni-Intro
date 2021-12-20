numbers = input().split(" ")
new_numbers = []
for num in numbers:
    temp = num
    temp = int(temp)
    temp = temp * -1
    new_numbers.append(temp)
print(new_numbers)