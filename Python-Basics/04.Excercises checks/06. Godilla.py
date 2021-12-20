budget = float(input())
humans = int(input())
price_dress = float(input())

decor_price = budget * 0.10

price_dress = price_dress * humans

if humans > 150:
    price_dress -= price_dress * 0.10

sum = decor_price + price_dress
if budget >= sum:
    print ("Action!")
    budget = budget - sum
    print (f"Wingard starts filming with {budget:.2f} leva left.")
elif budget <= sum:
    print ("Not enough money!")
    sum = sum - budget
    print (f"Wingard needs {sum:.2f} leva more.")
