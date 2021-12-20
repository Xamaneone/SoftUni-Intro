numbers = int(input())
IsTrue = 1<=numbers<=1000
p1_counter = 0
p2_counter = 0
p3_counter = 0

for i in range(0, numbers):
    number = int(input())
    if number % 2 == 0:
        p1_counter += 1
    if number % 3 == 0:
        p2_counter += 1
    if number % 4 == 0:
        p3_counter += 1
p1_counter = p1_counter / numbers * 100
p2_counter = p2_counter / numbers * 100
p3_counter = p3_counter / numbers * 100
if IsTrue:
    print(f"{p1_counter:.2f}%")
    print(f"{p2_counter:.2f}%")
    print(f"{p3_counter:.2f}%")