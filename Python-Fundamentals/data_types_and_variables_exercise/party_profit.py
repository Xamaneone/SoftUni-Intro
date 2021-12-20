party_size = int(input())
days = int(input())
coins = 0
for day in range(1, days + 1):
    if day % 10 == 0:
        party_size -= 2
    if day % 15 == 0:
        party_size += 5
    coins += 50
    coins -= party_size * 2  # spent for food
    if day % 3 == 0:
        coins -= party_size * 3  # spent for water
    if day % 5 == 0:
        coins += 20 * party_size  # monster slay
        if day % 3 == 0:
            coins -= party_size * 2

print(f"{party_size} companions received {int(coins / party_size)} coins each.")