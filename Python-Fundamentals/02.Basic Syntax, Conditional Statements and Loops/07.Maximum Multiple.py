divisor = int(input())
bound = int(input())
number = 0
answer = 0
huh = 0
for i in range(0, bound):
    number += 1
    answer = divisor * number
    if answer > bound:
        break
    huh = answer
print(huh)