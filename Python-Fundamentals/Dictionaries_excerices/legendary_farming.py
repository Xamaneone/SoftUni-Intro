Legendary_items = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
key_materials = {"shards": 0, "fragments": 0, "motes": 0}
keys = ["shards", "fragments", "motes"]
junk = {}
temp = []
result = []
we_done = False
while True:
    data = input().split(" ")
    for counter in range(0, len(data), 2):
        quantity = int(data[counter])
        material = data[counter + 1]
        material = material.lower()
        if material in keys and material in key_materials:
            key_materials[material] += quantity
        elif material in keys:
            key_materials[material] = quantity
        elif material in junk:
            junk[material] += quantity
        elif material not in junk:
            junk[material] = quantity
        for key, materials in key_materials.items():
            if materials >= 250:
                temp.append(key)
                we_done = True
        if we_done is not True:
            continue
        else:
            break
    if we_done is not True:
        continue
    else:
        break


temp.sort()
for word in temp:
    key_materials[word] -= 250
    print(f"{Legendary_items[word]} obtained!")
temp.clear()
for material, quantity in sorted(key_materials.items(), key=lambda x: (-x[1], x[0])):
    print(f"{material}: {quantity}")
temp.sort()
for material in temp:
    print(f"{material}: {key_materials[material]}")
temp.clear()
for material in junk.keys():
    temp.append(material)
temp.sort()
for material in temp:
    print(f"{material}: {junk[material]}")



# temp.sort()
# for word in temp:
#     key_materials[word] -= 250
#     print(f"{Legendary_items[word]} obtained!")
# temp.clear()
# for material in key_materials.keys():
#     temp.append(material)
# temp.sort()
# for material in temp:
#     print(f"{material}: {key_materials[material]}")
# temp.clear()
# for material in junk.keys():
#     temp.append(material)
# temp.sort()
# for material in temp:
#     print(f"{material}: {junk[material]}")