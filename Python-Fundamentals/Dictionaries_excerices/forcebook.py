sides = {}

data = input()



while not data == "Lumpawaroo":
    keep_it = True
    idk = False
    if "|" in data:
        side, name = data.split(" | ")
        if side in sides:
            for person in sides[side]:
                if name in person:
                    idk = True
                    break
                idk = True
        if side not in sides and name not in sides.keys():
            sides[side] = [name]
        if idk is True:
            sides[side].append(name)
    elif " -> " in data:
        name, side = data.split(" -> ")
        for Side, Name in sides.items():
            if name in Name:
                sides[Side].remove(name)
                sides[side].append(name)
                print(f"{name} joins the {side} side!")
                keep_it = False
                break
        if keep_it is True:
            for Side, Name in sides.items():
                if name not in Name and len(sides.get(Side)) != None:
                    sides[side].append(name)
                    print(f"{name} joins the {side} side!")
                    break
                elif name not in Name:
                    sides[side] = [name]
                    print(f"{name} joins the {side} side!")
                    break

    data = input()
    continue

for side, name in sorted(sides.items(), key=lambda x: (-len(x[1]), x[0])):
    if 0 == len(name):
        continue
    else:
        print(f"Side: {side}, Members: {len(name)}")
        for person in sorted(name):
            print(f"! {person}")
