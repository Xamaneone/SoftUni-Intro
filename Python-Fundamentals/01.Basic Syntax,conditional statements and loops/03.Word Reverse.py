word = input()
drow = ""
for i in range(len(word) - 1, -1, -1):
    drow += word[i]
print(drow)