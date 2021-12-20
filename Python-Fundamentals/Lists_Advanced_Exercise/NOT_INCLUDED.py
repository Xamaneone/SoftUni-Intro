temp = input().split(" ")
years = 0

Limak, Bob = temp
Limak, Bob = int(Limak), int(Bob)

while Limak <= Bob:
    Limak = Limak * 3
    Bob = Bob * 2
    years += 1
print(years)
