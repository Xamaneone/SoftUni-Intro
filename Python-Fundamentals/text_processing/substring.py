keyword = input()
word = input()
while keyword in word:
    word = word.split(keyword)
    temp = ""
    for string in word:
        temp += string
    word = temp
print(word)
