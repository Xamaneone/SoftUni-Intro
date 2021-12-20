word = input()

s = []

for chr in word:
    s.append(chr)

result = ""

while s:
    result += s.pop()

print(result)
