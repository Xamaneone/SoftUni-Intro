entry = input().split(" ")
data = ""
for i in entry:
    data += i
result = {}
for char in data:
    if char in result:
        result[char] += 1
    else:
        result[char] = 1

for char, count in result.items():
    print(f"{char} -> {count}")
