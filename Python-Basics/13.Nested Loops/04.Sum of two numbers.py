first = int(input())
second = int(input())
magic_number = int(input())
combinations = 0
hey = False
for f in range(first, second + 1, 1):
    for s in range(first, second + 1, 1):
        if hey is True:
            break
        combinations += 1
        if f + s == magic_number:
            print (f"Combination N:{combinations} ({f} + {s} = {magic_number})")
            hey = True
if hey is False:
    print (f"{combinations} combinations - neither equals {magic_number}")
