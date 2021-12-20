nights = int(input()) - 1
room = input()
grade = input()
nights_original = nights
if room == "room for one person":
    nights *= 18

elif room == "apartment":
    nights *= 25
    if 10 >= nights_original:
        nights -= nights * 0.30
    elif 10 <= nights_original <= 15:
        nights -= nights * 0.35
    elif nights_original >= 15:
        nights -= nights * 0.50
elif room == "president apartment":
    nights *= 35
    if 10 >= nights_original:
        nights -= nights * 0.10
    elif 10 <= nights_original <= 15:
        nights -= nights * 0.15
    elif nights_original >= 15:
        nights -= nights * 0.20

if grade == "positive":
    nights += nights * 0.25
elif grade == "negative":
    nights -= nights * 0.10
print (f"{nights:.2f}")