days = int(input())
players = int(input())
cakes_number = int(input())
waffles_number = int(input())
pancakes_number = int(input())

cakes_price = 45 * cakes_number
waffles_price = 5.8 * waffles_number
pancakes_price = 3.20 * pancakes_number
SUM = (cakes_price + waffles_price + pancakes_price) * days
all = SUM * players
result = all - (1/8 * all)


print(result)




