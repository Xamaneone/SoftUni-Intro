keywords = input().split(", ")
text = input()

for keyword in keywords:
    text = text.replace(keyword, len(keyword) * "*")
print(text)

