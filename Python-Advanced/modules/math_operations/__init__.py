from .operations import add, divide, multiply, power, substract


def calculate_expression(expression):
    (x, sign, y) = expression.split(' ')
    x = float(x)
    y = int(y)
    result = None
    if sign == '+':
        result = add(x, y)
    elif sign == '-':
        result = substract(x, y)
    elif sign == '*':
        result = multiply(x, y)
    elif sign == '/':
        result = divide(x, y)
    elif sign == '^':
        result = power(x, y)
    return f'{result:.2f}'