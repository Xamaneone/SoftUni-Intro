def translate(data, char, replacement):
    result = data.replace(char, replacement)
    print(result)
    return result
def includes(data, string):
    if string in data:
        return True
    return False

def start(data, string):
    counter = 0
    is_it = False
    for char in string:
        if char == data[counter]:
            counter += 1
            is_it = True
            continue
        else:
            is_it = False
            break
    return is_it

def findindex(data, char):
    for i in range(0, len(data)):
        if char == data[i]:
            last_inedx = i
    return last_inedx


def remove(data, start_index, count):
    start_index = int(start_index)
    count = int(count)
    stop_index = int(start_index) + int(count)
    if len(data) > stop_index:
        data = data[0: start_index:] + data[stop_index + 0::]
    print(data)
    return data




data = input()

command = input()

while command != "End":
    command = command.split()
    if command[0] == "Lowercase":
        data = data.lower()
        print(data)
        command = input()
        continue

    elif len(command) == 2:
        act = command[0]
        a = command[1]
    elif len(command) == 3:
        act = command[0]
        a = command[1]
        b = command[2]

    if act == "Translate":
        data = translate(data, a, b)
    elif act == "Includes":
        print(includes(data, a))
    elif act == "Start":
        print(start(data, a))
    elif act == "FindIndex":
        print(findindex(data, a))
    elif act == "Remove":
        data = remove(data, a, b)


    command = input()