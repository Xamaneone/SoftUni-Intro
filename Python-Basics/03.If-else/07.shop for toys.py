puzzel = 2.60
doll = 3
bear = 4.10
minion = 8.20
train = 2

trip_price = float(input())

puzzel_count = int(input())
doll_count = int(input())
bear_count = int(input())
minion_count = int(input())
train_count = int(input())

income = puzzel_count * puzzel + doll_count * doll + bear * bear_count + minion * minion_count + train * train_count

total_toys = puzzel_count + doll_count + bear_count + minion_count + train_count

if total_toys >= 50:
    income -= income * 0.25

income -= income * 0.1

if income >= trip_price:
    print (f'Yes! {income - trip_price:.2f} lv left.')
else:
    print (f"Not enough money! {trip_price - income:.2f} lv needed.")