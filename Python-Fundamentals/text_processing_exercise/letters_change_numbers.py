def true_position(letter):
    return ord(letter.lower()) - 96



def letter_exploit_first(letter, number):
    if letter.isupper():
        return number / true_position(letter)
    else:
        return number * true_position(letter)


def letter_exploit_second(letter, result):
    if letter.isupper():
        result += -(true_position(letter))
        return result
    else:
        result += true_position(letter)
        return result

def divide(string):
    a = string[0]
    c = string[-1]
    b = string.replace(a, "")
    b = b.replace(c, "")
    b = float(b)
    return a, b, c

sum = 0
data = input().split()
for word in data:
    a, b, c = divide(word)
    b = letter_exploit_first(a, b)
    b = letter_exploit_second(c, b)
    sum += b
print(f"{sum:.2f}")