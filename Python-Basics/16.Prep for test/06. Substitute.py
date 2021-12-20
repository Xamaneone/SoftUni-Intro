k = int(input())
l = int(input())
m = int(input())
n = int(input())
count = 0
for f in range(k, 8 + 1):
    for s in range(9, l - 1, -1):
        for j in range(m, 8 + 1):
            for h in range(9, n - 1, -1):
                first = str(f) + str(s)
                second = str(j) + str(h)
                if f%2==0 and s%2==1 and j%2==0 and h%2==1:
                    if first != second:
                        count += 1
                        print(f"{f}{s} - {j}{h}")
                        if count == 6:
                            break
                    else:
                        print(f'Cannot change the same player.')
            if count == 6:
                break
        if count == 6:
            break
    if count == 6:
        break

