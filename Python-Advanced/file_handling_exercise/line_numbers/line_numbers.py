with open('text.txt') as file:
    current_line = 1
    symbols = ["?", "!", ".", ",", "'", "-"]
    output = []
    for line in file.readlines():
        line = line.replace("\n", "")
        punctuation_marks = 0
        letters = 0
        for char in line:
            if char in symbols:
                punctuation_marks += 1
            if char.isalpha():
                letters += 1
        output.append(f"Line {current_line}: {line} ({letters})({punctuation_marks})\n")

        current_line += 1

with open('output.txt', 'w') as file:
    for line in output:
        file.write(line)
