num = int(input())
for f in range(0, num):
    for s in range(0, num):
        for t in range(0, num):
            print(f"{chr(97 + f)}{chr(97 + s)}{chr(97 + t)}")