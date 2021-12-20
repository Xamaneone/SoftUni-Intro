rooms = int(input())
free_chairs = 0
game_over = False
for room in range(1, rooms + 1):
    data = input().split(" ")
    taken = int(data[1])
    chairs = int(len(data[0]))
    if taken > chairs:
        chairs_needed = taken - chairs
        print(f"{chairs_needed} more chairs needed in room {room}")
        game_over = True
        continue
    else:
        free_chairs += chairs - taken
if game_over is not True:
    print(f"Game On, {free_chairs} free chairs left")