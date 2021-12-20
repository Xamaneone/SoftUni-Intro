from _collections import deque


sequence = deque()

queries = int(input())
num = -1


while True:
    num += 1
    if num == queries:
        break
    else:
        command = input()
        if command.startswith("1 "):
            command = command.split(" ")
            sequence.appendleft(int(command[1]))
        else:
            command = int(command)
            if len(sequence) == 0:
                continue
            elif command == 2:
                sequence.popleft()
            elif command == 3:
                print(max(sequence))
            elif command == 4:
                print(min(sequence))

result = ""
lenght = len(sequence)
c = 0
for string in sequence:
    result += str(string)
    c += 1
    if c == lenght:
        break
    else:
        result += ", "


print(result)