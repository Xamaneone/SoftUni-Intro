budget = float(input())
circuits = input()
fan_card = input()
type = input()
price = ""
if circuits == "five":
    if type == "Child":
        price = 7
    if type == "Junior":
        price = 9
    if type == "Adult":
        price = 12
    if type == "Profi":
        price = 18
if circuits == "ten":
    if type == "Child":
        price = 11
    if type == "Junior":
        price = 16
    if type == "Adult":
        price = 21
    if type == "Profi":
        price = 32
if fan_card == "yes":
    price -= price * 0.20

if budget >= price:
    print(f"You bought {type} ticket for {circuits} laps. Your change is {budget - price:.2f}lv.")
else:
    print(f"You don't have enough money! You need {price - budget:.2f}lv more.")