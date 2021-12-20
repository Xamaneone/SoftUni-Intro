height = int(input())
apartments = int(input())
is_first = True
isit = 0
for f in range(height, 0, -1):
    for s in range(0, apartments, 1):
        if is_first == True:
            isit += 1
            print(f"L{f}{s}", end=" ")
            if isit == apartments:
                is_first = False
                continue
        if is_first == False:
            if f % 2 == 0:
                print(f"O{f}{s}", end=" ")
            else:
                print(f"A{f}{s}", end=" ")
    print(end="\n")
