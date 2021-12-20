data = input()
result = ""
demolish = 0
step = 0
Demolish = False
for word in data:
    if demolish > 0:
        Demolish = True
        demolish -= 1
    else:
        Demolish = False
    step += 1
    if Demolish is True:
        if word == ">":
            result += ">"
            demolish += int(data[step]) + 1
            continue
        else:
            continue

    if word == ">" and Demolish is False:
        result += ">"
        demolish += int(data[step])
        continue
    elif Demolish is False:
        if demolish == 0:
            result += word

print(result)