def slasher(data):
    list(data)
    number = []
    word = []
    for el in data:
        if el in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
            number.append(el)
        else:
            word.append(el)
    new_number = ""
    for num in number:
        new_number += str(num)
    new_number = int(new_number)
    number = chr(new_number)
    last = len(word) - 1
    word[0], word[last] = word[last], word[0]
    new_word = ""
    for letter in word:
        new_word += letter
    result = number + new_word
    return result
data = input().split(" ")
for i in range(0, len(data)):
    print(slasher(data[i]), end=" ")
