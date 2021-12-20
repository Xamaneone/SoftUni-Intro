disel_per_liter = 2.10
budget = float(input())
disel_needed = float(input())
day = input()
discount = 100
disel_needed = disel_needed * disel_per_liter
disel_needed += discount  # ексурзовод
if day == "Sunday":
    discount = disel_needed * 0.20
    round(discount, 2)
    disel_needed -= discount
    if budget >= disel_needed:
        print(f"Safari time! Money left: {budget - disel_needed:.2f} lv.")
    else:
        print(f"Not enough money! Money needed: {disel_needed - budget:.2f} lv.")
elif day == "Saturday":
    discount = disel_needed * 0.10
    disel_needed -= discount
    if budget >= disel_needed:
        print(f"Safari time! Money left: {budget - disel_needed:.2f} lv.")
    else:
        print(f"Not enough money! Money needed: {disel_needed - budget:.2f} lv.")
