heart = input().split("@")
hearts = [int(hearts) for hearts in heart]
position = 0
command = input().split(" ")
neighbourhoods = len(hearts)
while command[0] != "Love!":
    jump = int(command[1])
    position += jump
    if position >= len(hearts):
        position = 0
    if hearts[position] == 0:
        print(f"Place {position} already had Valentine's day.")
        command = input().split(" ")
        continue
    hearts[position] -= 2
    if hearts[position] == 0:
        print(f"Place {position} has Valentine's day.")
    command = input().split(" ")
# hearts.remove(0)
print(f"Cupid's last position was {position}.")
hearts = [i for i in hearts if i != 0]
if len(hearts) == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(hearts)} places.")



