def perfect_number(number):
    printing = "It's not so perfect."
    checker = number
    nums = 0
    proper_devisors_sum = 0
    for num in range(1, int(checker)):
        if int(checker) % num == 0:
            nums += int(num)
    if nums == int(checker):
        printing = "We have a perfect number!"
    return printing

print(perfect_number(str(input())))