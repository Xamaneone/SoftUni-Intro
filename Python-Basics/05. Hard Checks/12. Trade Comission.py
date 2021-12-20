city = input()
comission = float(input())
profit = comission
if comission < 0:
    print ("error")
elif "Sofia" == city:
    if 0 <= comission <= 500:
        comission *= 0.05
    elif 500 <= comission <= 1000:
        comission *= 0.07
    elif 1000 <= comission <= 10000:
        comission *= 0.08
    elif comission > 10000:
        comission *= 0.12
elif "Varna" == city:
    if 0 <= comission <= 500:
        comission *= 0.045
    elif 500 <= comission <= 1000:
        comission *= 0.075
    elif 1000 <= comission <= 10000:
        comission *= 0.1
    elif comission > 10000:
        comission *= 0.13
elif "Plovdiv" == city:
    if 0 <= comission <= 500:
        comission *= 0.055
    elif 500 <= comission <= 1000:
        comission *= 0.08
    elif 1000 <= comission <= 10000:
        comission *= 0.12
    elif comission > 10000:
        comission *= 0.145

if profit == comission:
    print ("error")
else:
    print (f"{comission:.2f}")


