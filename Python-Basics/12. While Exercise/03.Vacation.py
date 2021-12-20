price = float(input())
wallet = float(input())
spend_counter = 0
days_counter = 0

while True:
    days_counter += 1
    if price <= wallet:
        print(f"You saved the money for {days_counter} days.")
        break
    act = input()
    if act == "spend":
        spend_counter += 1
        if spend_counter == 5:
            print ("You can't save the money.")
            print (days_counter)
            break
        money = float(input())
        wallet -= money
        if wallet < 0:
            wallet = 0
    if act == "save":
        money = float(input())
        wallet += money
        spend_counter = 0

    if wallet >= price:
        print (f"You saved the money for {days_counter} days.")
        break