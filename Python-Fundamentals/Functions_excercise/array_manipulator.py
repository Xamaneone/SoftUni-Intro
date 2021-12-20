def exchange(elements, act):
    if int(act[1]) < 0:
        return "Invalid index"
    elif abs(int(act[1])) >= len(elements):
        return "Invalid index"
    reformated_array = []
    for array in range(abs(int(act[1])) + 1, len(elements)):
        reformated_array.append(elements[array])
    for array in range(0, abs(int(act[1])) + 1):
        reformated_array.append(elements[array])
    return reformated_array


def max_num(elements, act):
    num = -999
    if act[1] == "even":
        for element in elements:
            if int(element) % 2 == 0:
                if int(element) > num:
                    num = int(element)
    elif act[1] == "odd":
        for element in elements:
            if int(element) % 2 == 1:
                if int(element) > num:
                    num = int(element)
    if num == -999:
        return "No matches"
    for i in range(len(elements) - 1, -1, -1):
        if int(num) == int(elements[i]):
            return i


def min_num(elements, act):
    num = 999
    if act[1] == "even":
        for element in elements:
            if int(element) % 2 == 0:
                if int(element) < num:
                    num = int(element)
    elif act[1] == "odd":
        for element in elements:
            if int(element) % 2 == 1:
                if int(element) < num:
                    num = int(element)
    if num == 999:
        return "No matches"
    result = None
    for i in range(0, len(elements)):
        if int(num) == int(elements[i]):
            result = i
    return result



def first_num(elements, act):
    counter = 0
    result_list = []
    if int(act[1]) < 0:
        return "Invalid count"
    if int(act[1]) > len(elements):
        return "Invalid count"
    if int(act[1]) == 0:
        return result_list
    for array in elements:
        if act[2] == "even":
            if int(array) % 2 == 0:
                result_list.append(int(array))
                counter += 1
                if counter == abs(int(act[1])):
                    return result_list
                continue
        elif act[2] == "odd":
            if int(array) % 2 == 1:
                result_list.append(int(array))
                counter += 1
                if counter == abs(int(act[1])):
                    return result_list
    return result_list


def last_num(elements, act):
    counter = 0
    result_list = []
    if int(act[1]) < 0:
        return "Invalid count"
    if int(act[1]) > len(elements):
        return "Invalid count"
    if int(act[1]) == 0:
        return result_list
    for array in elements:
        if act[2] == "even":
            if int(array) % 2 == 0:
                result_list.append(int(array))
                counter += 1
        elif act[2] == "odd":
            if int(array) % 2 == 1:
                result_list.append(int(array))
                counter += 1
    for i in range(counter, abs(int(act[1])), -1):
        result_list.pop(0)
    return result_list

initial_array = input().split(" ")
data = None
while data != "end":
    data = input()
    if data == "end":
        result = []
        for array in initial_array:
            result.append(int(array))
        print(result)
        break
    data_list = data.split(" ")
    if data_list[0] == "exchange":
        temp = exchange(initial_array, data_list)
        if len(temp) == len(initial_array):
            initial_array = temp.copy()
        else:
            print(temp)
    elif data_list[0] == "max":
        print(max_num(initial_array, data_list))
    elif data_list[0] == "min":
        print(min_num(initial_array, data_list))
    elif data_list[0] == "first":
        print(first_num(initial_array, data_list))
    elif data_list[0] == "last":
        print(last_num(initial_array, data_list))
