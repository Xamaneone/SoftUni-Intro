days = int(input())
hours = int(input())
per_day = 0
total = 0
for d in range(1, days+1):
    for h in range(1, hours+1):
        if d % 2 == 0:
            if h % 2 == 0:
                per_day += 1
            else:
                per_day += 2.50
        else:
            if h % 2 == 0:
                per_day += 1.25
            else:
                per_day += 1
    print(f"Day: {d} - {per_day:.2f} leva")
    total += per_day
    per_day = 0
print(f"Total: {total:.2f} leva")
