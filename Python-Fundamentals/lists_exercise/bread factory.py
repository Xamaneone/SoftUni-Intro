data = input().split("|")
energy = 100
wallet = 100
passing = True
for temp in data:
    act, coins = temp.split("-")
    coins = int(coins)
    if act == "rest":
        recovery = 0
        if coins + energy <= 100:
            energy += coins
            recovery = coins
        else:
            recovery = 0
        print(f"You gained {recovery} energy.")
        print(f"Current energy: {energy}.")
    elif act == "order":
        if energy >= 30:
            energy -= 30
            wallet += coins
            print(f"You earned {coins} coins.")
        else:
            energy += 50
            print(f"You had to rest!")
            continue
    else:
        if wallet > coins:
            print(f"You bought {act}.")
            wallet -= coins
        else:
            print(f"Closed! Cannot afford {act}.")
            passing = False
            break

if passing is True:
    print(f"Day completed!")
    print(f"Coins: {wallet}")
    print(f"Energy: {energy}")