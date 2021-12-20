line = input()
result = "."
for word in line:
    if word != result[-1]:
        result += word
print(result.replace(".", ""))