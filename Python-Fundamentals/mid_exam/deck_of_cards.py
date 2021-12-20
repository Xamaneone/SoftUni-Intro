vehicles = input().split(", ")
n = int(input())
for i in range(0, n):
    act = input().split(", ")
    if act[0] == "Add":
        if act[1] in vehicles:
            print("Card is already bought")
        else:
            print("Card successfully bought")
            vehicles.append(act[1])
    elif act[0] == "Remove":
        if act[1] in vehicles:
            vehicles.remove(act[1])
            print("Card successfully sold")
        else:
            print("Card not found")
    elif act[0] == "Remove At":
        if 0 <= int(act[1]) < len(vehicles):
            vehicles.pop(int(act[1]))
            print(f"Card successfully sold")
        else:
            print("Index out of range")
    elif act[0] == "Insert":
        if 0 <= int(act[1]) < len(vehicles):
            if act[2] in vehicles:
                print("Card is already bought")
            else:
                vehicles.insert(int(act[1]), act[2])
                print("Card successfully bought")
        else:
            print("Index out of range")
print(*vehicles, sep=", ")
