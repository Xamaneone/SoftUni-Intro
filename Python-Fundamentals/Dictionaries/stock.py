data = input().split(" ")
bakery = {}
for index in range(0, len(data), 2):
    key = data[index]
    value = int(data[index + 1])
    bakery[key] = value


products_to_search = input().split(" ")
for product in products_to_search:
    if product in bakery:
        print(f"We have {bakery[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
