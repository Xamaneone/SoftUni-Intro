from _collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = deque(input().split(" "))
locks = deque(input().split(" "))
intelligence_value = int(input())

balance = 0

Sam = True
Lockers = True

while True:
    if bullets and locks:
        for gun_barrel in range(gun_barrel_size):
            if bullets:
                bullet = int(bullets.pop())
            else:
                Sam = False
                break
            if locks:
                lock = int(locks.popleft())
            else:
                Lockers = False
                break
            if bullet <= lock:
                print("Bang!")
            else:
                locks.appendleft(str(lock))
                print("Ping!")
            intelligence_value -= bullet_price

    if not locks:
        Lockers = False


    if not bullets:
        Sam = False

    if not Lockers:
        if bullets:
            print("Reloading!")
        print(f"{len(bullets)} bullets left. Earned ${intelligence_value}")
        break
    if not Sam:
        print(f"Couldn't get through. Locks left: {len(locks)}")
        break

    print("Reloading!")