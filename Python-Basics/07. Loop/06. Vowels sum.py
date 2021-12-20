text = input()
sum = 0
for index in range(0, len(text)):
    symbol = text[index]

    if symbol == "a" or symbol == "A":
        sum += 1
    elif symbol == "e" or symbol == "E":
        sum += 2
    elif symbol == "i" or symbol == "I":
        sum += 3
    elif symbol == "o" or symbol == "O":
        sum += 4
    elif symbol == "u" or symbol == "U":
        sum += 5

print (sum)

