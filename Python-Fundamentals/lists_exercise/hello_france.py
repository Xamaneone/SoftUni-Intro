data = input().split("|")
budget = float(input())
profit = 0
temp = 0
temp2 = 0
temp2 = budget
for info in data:
    Type, Price = info.split("->")
    Price = float(Price)
    if Type == "Clothes" and Price > 50.00:
        continue
    elif Type == "Shoes" and Price > 35.00:
        continue
    elif Type == "Accessories" and Price > 20.50:
        continue
    if budget < Price:
        continue
    budget -= Price
    # Price, profit = Price * 1.40, Price * 1.40 - Price
    temp = Price
    Price = Price * 1.40
    profit += Price - temp
    print(f"{Price:.2f}", end=" ")
print(f"\nProfit: {profit:.2f}")
temp2 += profit
if temp2 >= 150.00:
    print("Hello, France!")
else:
    print("Time to go.")




