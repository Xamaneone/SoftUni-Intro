quantity = int(input())
days = int(input())
totalspirit = 0
last_day = 0
budget = 0
for i in range(1, days + 1):
    if i % 11 == 0:
        quantity += 2
    if i % 2 == 0:
        budget += quantity * 2
        totalspirit += 5
    if i % 3 == 0:
        budget += (quantity * 5) + (quantity * 3)
        totalspirit += 13
    if i % 5 == 0:
        budget += quantity * 15
        totalspirit += 17
        if i % 3 == 0:
            totalspirit += 30
    if i % 10 == 0:
        totalspirit -= 20
        budget += 23
    last_day = i
if last_day % 10 == 0:
    totalspirit -= 30
print(f"Total cost: {budget}")
print(f"Total spirit: {totalspirit}")