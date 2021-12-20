wagons = int(input())
wagons_of_train = [0 for _ in range(wagons)]

commande = input()
while commande != "End":
    command = commande.split()
    if command[0] == "add":
        number_of_people = int(command[1])
        wagons_of_train[-1] += number_of_people
    elif command[0] == "insert":
        index = int(command[1])
        wagons_of_train[index] += int(command[2])
    elif command[0] == "leave":
        index = int(command[1])
        wagons_of_train[index] -= int(command[2])
    commande = input()
print(wagons_of_train)