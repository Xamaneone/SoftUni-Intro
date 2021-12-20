import re

def get_file_content(file):
    with open(file) as file:
        text = ''.join(file.readlines())
        return re.findall(r"[a-z']+", text.lower())

def write_result(res):
    with open('Words Count/output.txt', 'w') as file:
        for r in res:
            file.write(r+"\n")

path_to_words = 'Words Count/words.txt'
path_to_text = 'Words Count/text.txt'

first_file = get_file_content(path_to_words)
second_file = get_file_content(path_to_text)
analyse = {}

for word in first_file:
    if word in second_file:
        analyse[word] = second_file.count(word)

result = ([f"{el[0]} - {el[1]}" for el in sorted(analyse.items(), key=lambda x: -x[1])])
print(result)

write_result(result)