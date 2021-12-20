first_string = input()
second_string = input()
result = ""
last = first_string
for iteration in range(len(first_string)):
    for second in range(0, iteration + 1):
        result += second_string[second]
    for first in range(iteration + 1, len(first_string)):
        result += first_string[first]
    if not last == result:
        print(result)
    last = result
    result = ""