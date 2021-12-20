def odd_and_even_sum(numbers):
    odd = 0
    even = 0
    numbers.split()
    for num in numbers:
        if int(num) % 2 == 0:
            even += int(num)
        else:
            odd += int(num)
    print(f"Odd sum = {odd}, Even sum = {even}")

odd_and_even_sum(str(input()))