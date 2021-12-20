cappacity = 0
lines = int(input())
for i in range(0, lines):
    water = int(input())
    if cappacity + water > 255:
        print("Insufficient capacity!")
        continue
    else:
        cappacity += water
print(cappacity)