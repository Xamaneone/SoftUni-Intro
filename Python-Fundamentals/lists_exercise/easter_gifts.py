gifts = input().split(" ")
while True:
    command = input().split(" ")
    if command[0] == "No":
        break
    else:
        a = None
    if command[0] == "OutOfStock":
        for i in range(0,len(gifts)):
            if gifts[i] == command[1]:
                gifts[i] = None
    elif command[0] == "JustInCase":
        gifts[-1] = command[1]
    elif command[0] == "Required":
        if 0 < int(command[2]) < len(gifts):
            gifts[int(command[2])] = command[1]
for gift in gifts:
    if gift == None:
        continue
    else:
        print(gift, end=" ")