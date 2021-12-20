def add_and_subtract(num1, num2, num3):
    def sum_numbers(num1, num2):
        result = num1 + num2
        return result
    def subtract(result, num3):
        result = result - num3
        return result
    result = subtract(sum_numbers(num1, num2), num3)
    return result
print(add_and_subtract(int(input()), int(input()), int(input())))