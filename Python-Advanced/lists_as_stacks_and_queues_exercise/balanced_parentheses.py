from _collections import deque

INPUT = input()


data = deque()


for parenthesis in INPUT:
    if parenthesis == "{" or parenthesis == "[" or parenthesis == "(":
        data.append(parenthesis)
    if parenthesis == "}" or parenthesis == "]" or parenthesis == ")":
        if len(data) == 0:
            data.append("Nope")
            break
    if parenthesis == "}":
        if data.pop() != "{":
            break
    elif parenthesis == "]":
        if data.pop() != "[":
            break
    elif parenthesis == ")":
        if data.pop() != "(":
            break

if len(data) == 0:
    print("YES")
else:
    print("NO")