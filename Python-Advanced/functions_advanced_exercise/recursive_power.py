def recursive_power(num, power, sum=1):
    if power == 0:
        return sum
    num *= recursive_power(num, power - 1)
    return num



print(recursive_power(2, 10))
print(recursive_power(10, 100))