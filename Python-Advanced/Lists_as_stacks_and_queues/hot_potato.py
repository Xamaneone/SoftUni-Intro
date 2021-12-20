from _collections import deque

players = deque(input().split(" "))
hot_num = int(input())

while len(players) != 1:
    n = 1
    while n != hot_num:
        players.append(players.popleft())
        n += 1
    print(f"Removed {players.popleft()}")


print(f"Last is {''.join(players)}")