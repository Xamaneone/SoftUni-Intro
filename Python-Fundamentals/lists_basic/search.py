cycle = int(input())
keyword = input()
without_keyword = []
with_keyword = []
for i in range(cycle):
    text = input()
    without_keyword.append(text)
    if text.find(keyword) != -1:
        with_keyword.append(text)
print(without_keyword)
print(with_keyword)