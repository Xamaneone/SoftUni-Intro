digits = []
letters = []
others = []

text = input()

for letter in text:
    if letter.isdigit():
        digits.append(letter)
    elif letter.isalpha():
        letters.append(letter)
    else:
        others.append(letter)

print("".join(digits))
print("".join(letters))
print("".join(others))