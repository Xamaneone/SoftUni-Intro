strikes = input().split(" ")
A = []
B = []
strike_A = []
strike_B = []
for i in range(1, 12):
    A.append(i)
    B.append(i)
for strike in strikes:
    team, player = strike.split("-")
    if team == "A":
        if player in strike_A:
            continue
        else:
            strike_A.append(player)
    elif team == "B":
        if player in strike_B:
            continue
        else:
            strike_B.append(player)
    if len(A) - len(strike_A) < 7 or len(B) - len(strike_B) < 7 :
        break
if 11 - len(strike_A) < 7 or 11 - len(strike_B) < 7:
    finished = True
    print(f"Team A - {len(A) - len(strike_A)}; Team B - {len(B) - len(strike_B)}")
    print(f"Game was terminated")
else:
    print(f"Team A - {len(A) - len(strike_A)}; Team B - {len(B) - len(strike_B)}")
