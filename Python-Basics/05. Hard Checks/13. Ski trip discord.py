days = int(input())
roomtype = input()
rating = input()
nights = days - 1
discount = 0
price = 0
if roomtype == "room for one person":
    price = 18 * nights
elif roomtype == "apartment":
    price = 25 * nights
    if days < 10:
        discount = 0.30
    elif 10 <= days <= 15:
        discount = 0.35
    elif days > 15:
        discount = 0.50
    price -= price * discount
elif roomtype == "president apartment":
    price = 35 * nights
    if days < 10:
        discount = 0.10
    elif 10 <= days <= 15:
        discount = 0.15
    elif days > 15:
        discount = 0.20
    price -= price * discount
if rating == "positive":
    price += price * 0.25
else:
    price -= price * 0.10
print(f"{price:.2f}")