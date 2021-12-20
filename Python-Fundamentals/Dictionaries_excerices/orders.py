products_prices = {}
products_quantities = {}

data = input()

while not data == "buy":
    product, price, quantity = data.split(" ")
    price = float(price)
    quantity = int(quantity)
    if product not in products_prices:
        products_prices[product] = price
        products_quantities[product] = quantity
    else:
        products_prices[product] = price
        products_quantities[product] += quantity


    data = input()

for product in products_prices:
    price = products_prices[product] * products_quantities[product]
    print(f"{product} -> {price:.2f} ")