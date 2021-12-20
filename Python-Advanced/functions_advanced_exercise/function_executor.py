from functools import reduce


def func_executor(*args):
    result = []
    for func_name, data in args:
        result.append(func_name(*data))
    return result

def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
