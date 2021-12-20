def factorial_division(num1, num2):
    sum = 1
    sum2 = 1
    for num in range(num1, 0, -1):
        sum = sum * num
    for num in range(num2, 0, -1):
        sum2 = sum2 * num
    result = sum / sum2
    return result




num1 = int(input())
num2 = int(input())
print(f"{factorial_division(num1, num2):.2f}")