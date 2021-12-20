#плод  - banana / apple / orange / grapefruit / kiwi / pineapple / grapes;
#ден от седмицата  - Monday / Tuesday / Wednesday / Thursday / Friday / Saturday / Sunday;
#количество (реално число).
product = input()
day = input()
quantity = float(input())
price = float(0)
if "Monday" == day or "Tuesday" == day or "Wednesday" == day or "Thursday" == day or "Friday" == day:
    if product == "banana":
        price = 2.50 * quantity
    elif product == "apple":
        price = 1.20 * quantity
    elif product == "orange":
        price = 0.85 * quantity
    elif product == "grapefruit":
        price = 1.45 * quantity
    elif product == "kiwi":
        price = 2.70 * quantity
    elif product == "pineapple":
        price = 5.50 * quantity
    elif product == "grapes":
        price = 3.85 * quantity
elif "Sunday" == day or "Saturday" == day:
    if product == "banana":
        price = 2.70 * quantity
    elif product == "apple":
        price = 1.25 * quantity
    elif product == "orange":
        price = 0.90 * quantity
    elif product == "grapefruit":
        price = 1.60 * quantity
    elif product == "kiwi":
        price = 3.00 * quantity
    elif product == "pineapple":
        price = 5.60 * quantity
    elif product == "grapes":
        price = 4.20 * quantity
if price != 0:
    print(f"{price:.2f}")
elif not price != 0:
    print("error")


