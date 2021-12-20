budget = float(input())
name = "Hello, there!"
count = 0
diff_count = 0
fee = 0
while True:
    name = input()
    if name == "Stop":
        print(f"You bought {count} products for {fee:.2f} leva.")
        break
    price = float(input())
    diff_count += 1
    if diff_count%3 == 0:
        price = price / 2
    if price > budget:
        print(f"You don't have enough money!")
        print (f"You need {price-budget:.2f} leva!")
        break
    budget -= price
    fee += price
    count += 1
