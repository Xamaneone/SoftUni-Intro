record = float(input())
distance = float(input())
time = float(input())
slowdown = ((distance // 15) * 12.5)
time *= distance
time += slowdown
fail = time - record
if fail < 0:
    fail = (-fail)
if record > time:
    print(f"Yes, he succeeded! The new world record is {time:.2f} seconds.")
else:
    print(f"No, he failed! He was {fail:.2f} seconds slower.")