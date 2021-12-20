def palindrome_check(numbers):
    for num in numbers.split(", "):
        value = ""
        num = str(num)
        for letter in range(len(num) - 1, -1, -1):
            value += str(num[letter])
        if num == value:
            print(True)
        else:
            print(False)


palindrome_check(str(input()))