def rev_sentence(sentence):
    words = sentence.split(' ')
    reverse_sentence = ' '.join(reversed(words))
    return reverse_sentence


with open('text.txt') as file:
    result = []
    line_counter = 0
    for line in file.readlines():
        if line_counter % 2 == 0:
            result.append(line.strip())
        line_counter += 1

symbols = ["-", ",", ".", "!", "?"]

for line in result:
    current_line = rev_sentence(line)
    for symbol in symbols:
        current_line = current_line.replace(symbol, "@")
    print(current_line)