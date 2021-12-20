budget = float(input())
flour = float(input())
eggs = flour * 0.75
milk_price = flour * 1.25
milk = milk_price * 0.25
cozonacs = 0
cost = flour + eggs + milk
colored_eggs = 0
cozonacs_counter = 1
while budget >= cost:
    budget -= cost
    cozonacs += 1
    colored_eggs += 3
    if cozonacs_counter % 3 == 0:
        # colored_eggs -= (cozonacs_counter - 2)
        colored_eggs -= cozonacs_counter - 2
    cozonacs_counter += 1
print(f"You made {cozonacs} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")