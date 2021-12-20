budget = float(input())
season = input()
fishers = float(input())
discount = 0
if season == "Summer" or season == "Autumn":
    boat_price = 4200
elif season == "Spring":
    boat_price = 3000
elif season == "Winter":
    boat_price = 2600

if fishers <= 6:
    discount += 0.10
elif fishers <= 11:
    discount += 0.15
elif fishers >= 12:
    discount += 0.25

if fishers % 2 == 0 and season != "Autumn":
    discount += 0.05
if discount != 0:
    boat_price -= boat_price*discount
if budget >= boat_price:
    budget -= boat_price
    print (f"Yes! You have {budget:.2f} leva left.")
else:
    boat_price -= budget
    print (f"Not enough money! You need {boat_price:.2f} leva.")


