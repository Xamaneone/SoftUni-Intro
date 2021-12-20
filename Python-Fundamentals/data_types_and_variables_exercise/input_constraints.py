lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
aureus = 0
armor_repair_counter = 0
for game in range (1, lost_fights_count + 1):
    if game % 2 == 0:
        aureus += helmet_price
    if game % 3 == 0:
        aureus += sword_price
    if game % 2 == 0 and game % 3 == 0:
        aureus += shield_price
        armor_repair_counter += 1
    if armor_repair_counter != 0:
        if armor_repair_counter % 2 == 0:
            aureus += armor_price
            armor_repair_counter = 0

print(f"Gladiator expenses: {aureus:.2f} aureus")