line = input()

party = {}
unlikes = 0

while line != "Stop":
    act, guest, meal = line.split("-")
    if act == "Like":
        if guest in party.keys():
            if meal in party[guest]:
                line = input()
                continue
            party[guest].append(meal)
            line = input()
            continue
        party[guest] = [meal]
    elif act == "Unlike":
        if guest not in party.keys():
            print(f"{guest} is not at the party.")
            line = input()
            continue
        elif meal not in party[guest]:
            print(f"{guest} doesn't have the {meal} in his/her collection.")
            line = input()
            continue
        else:
            party[guest].remove(meal)
            print(f"{guest} doesn't like the {meal}.")
            unlikes += 1
            line = input()
            continue
    line = input()
for member, foods in sorted(party.items(), key=lambda x: (-len(x[1]), x[0])):
    if len(foods) == 0:
        print(f"{member}:")
    else:
        print(f"{member}: {', '.join(foods)}")
print(f"Unliked meals: {unlikes}")