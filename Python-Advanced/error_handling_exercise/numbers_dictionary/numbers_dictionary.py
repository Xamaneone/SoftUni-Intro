def get_input():
    numbers_dict = {}
    command = str(input())
    while command != "Search":
        try:
            number = int(input())
        except ValueError:
            print('The variable number must be an integer')
            command = str(input())
            continue
        numbers_dict[command] = number
        command = str(input())
    return numbers_dict, command



def search_trough_dict(dict):
    number_as_string = input()
    try:
        number = dict.get(number_as_string)
        if number != None:
            print(number)
        return
    except TypeError:
        print('Number does not exist in dictionary')
        return


def remove_from_dict(dictonary):
    number_as_str = input()
    try:
        del dictonary[number_as_str]
        return dictonary
    except KeyError:
        print('Number does not exist in dictionary')
        return dictonary


numbers_dict, command = get_input()

while command != "End":
    if command == "Search":
        search_trough_dict(numbers_dict)
    elif command == "Remove":
        numbers_dict = remove_from_dict(numbers_dict)
    command = input()

print(numbers_dict)