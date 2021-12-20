data = input()

products = {}
while not data == "statistics":
    product, quantity = data.split(": ")
    quantity = int(quantity)
    if product in products:
        products[product] += quantity
    else:
        products[product] = quantity
    data = input()
print("Products in stock:")
for product in products:
    print(f"- {product}: {products[product]}")
print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")

