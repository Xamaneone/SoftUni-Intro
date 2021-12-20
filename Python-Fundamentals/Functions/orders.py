def order(product, quantity):
    price = None
    if product == "coffee":
        price = 1.50 * quantity
    elif product == "water":
        price = 1.00 * quantity
    elif product == "coke":
        price = 1.40 * quantity
    elif product == "snacks":
        price = 2.00 * quantity
    return price
product = input()
quantity = int(input())
print(f"{order(product, quantity):.2f}")
