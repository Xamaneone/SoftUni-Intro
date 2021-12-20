total = 0
money = input()
while money != "NoMoreMoney":
    money = float(money)
    if money < 0:
        print ("Invalid operation!")
        break
    else:
        print (f"Increase: {money:.2f}")
        total += money
        money = input()
print (f"Total: {total:.2f}")
