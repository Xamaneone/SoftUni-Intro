HIGH_RANGE = range(81, 126)
MEDIUM_RANGE = range(51, 81)
LOW_RANGE = range(1, 51)

effort = 0
put_out_fire = []

fire_data = input().split("#")
water_amount = int(input())
for fire in fire_data:
    type_of_fire, value = fire.split(" = ")
    value = int(value)

    if type_of_fire == "High" and value not in HIGH_RANGE:
        continue
    elif type_of_fire == "Medium" and value not in MEDIUM_RANGE:
        continue
    elif type_of_fire == "Low" and value not in LOW_RANGE:
        continue

    # TODO check if water is enough to

    if water_amount >= value:
        water_amount -= value
        effort += value * 0.25
        put_out_fire.append(value)

print("Cells:")
for fire in put_out_fire:
    print(f"- {fire}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {sum(put_out_fire)}")