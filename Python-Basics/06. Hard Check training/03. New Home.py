flower = input()
quantity = float(input())
wallet = float(input())
discount = 0
if flower == "Roses":
    price = 5
    if quantity > 80:
        discount = quantity * price * 0.10
elif flower == "Dahlias":
    price = 3.80
    if quantity > 90:
        discount = quantity * price * 0.15
elif flower == "Tulips":
    price = 2.80
    if quantity > 80:
        discount = quantity * price * 0.15
elif flower == "Narcissus":
    price = 3
    if quantity < 120:
        discount = quantity * price * 0.15
elif flower == "Gladiolus":
    price = 2.50
    if quantity < 80:
        discount = quantity * price * 0.20

if flower == "Roses" or flower == "Dahlias" or flower == "Tulips":
    if wallet >= price * quantity - discount:
        wallet -= price * quantity - discount
        print (f"Hey, you have a great garden with {round(quantity)} {flower} and {wallet:.2f} leva left.")
    elif wallet < price * quantity - discount:
        wallet = price * quantity - discount - wallet
        print (f"Not enough money, you need {wallet:.2f} leva more.")
elif flower == "Narcissus" or flower == "Gladiolus":
    if wallet >= price * quantity + discount:
        wallet -= price * quantity + discount
        print (f"Hey, you have a great garden with {round(quantity)} {flower} and {wallet:.2f} leva left.")
    elif wallet < price * quantity + discount:
        wallet = price * quantity + discount - wallet
        print (f"Not enough money, you need {wallet:.2f} leva more.")