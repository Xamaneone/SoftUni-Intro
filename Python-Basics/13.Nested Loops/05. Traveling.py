is_destination = False
while is_destination is False:
    destination = input()
    if destination == "End":
        is_destination = True
        break
    cost = float(input())
    wallet = float(0)
    while wallet < cost:
        wallet += float(input())
    print(f"Going to {destination}!")
