x = int(input())
z = int(input())
sum = int(0)

cake = x * z
while True:
    piece = input()
    if piece != "STOP":
        piece = float(piece)
        piece = int(piece)
        sum += piece
        if sum > cake:
            print (f"No more cake left! You need {sum - cake} pieces more.")
            break
    if piece == "STOP":
        if sum <= cake:
            print (f"{cake - sum} pieces are left.")
            break
        else:
            print (f"No more cake left! You need {sum - cake} pieces more.")
            break
