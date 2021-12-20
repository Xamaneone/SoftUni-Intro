employees = input().split(" ")
happiness_factor = int(input())

employees = list(map(lambda x: int(x) * happiness_factor, employees))
temp = sum(employees) / len(employees)

filtered = list(filter(lambda x: x >= temp, (employees)))

if len(filtered) >= len(employees) / 2:
    print(f"Score: {len(filtered)}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {len(filtered)}/{len(employees)}. Employees are not happy!")