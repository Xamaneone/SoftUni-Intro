def move(direction, index):
    if direction == "Left":
        if index <= 0 or index > len(strings):
            return
        strings.insert(index - 1, (strings.pop(index)))
        return
    if direction == "Right":
        if index >= len(strings) or index < 0:
            return
        strings.insert(index + 1, (strings.pop(index)))
        return

def check(type):
    result = []
    if type == "Even":
        for i in range(0, len(strings)):
            if i % 2 == 0:
                result.append(strings[i])
    elif type == "Odd":
        for i in range(0, len(strings)):
            if i % 2 != 0:
                result.append(strings[i])
    return result



strings = input().split("|")

command = input()
while command != "Done":
    command = command.split(" ")
    if command[0] == "Move":
        move(command[1], int(command[2]))
    if command[0] == "Check":
        print(*check(command[1]), sep=" ")
    command = input()
print(f"You crafted ", end="")
for string in strings:
    print(string, end="")
print("!")