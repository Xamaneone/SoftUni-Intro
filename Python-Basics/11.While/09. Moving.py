z = int(input())
y = int(input())
x = int(input())
space = x * y * z
box = int(0)
box_space = int(0)
while box != "Done":
    box = input()
    if box != "Done":
        box = float(box)
        box = int(box)
        box_space += box
    if box_space > space:
        print(f"No more free space! You need {box_space - space} Cubic meters more.")
        break
    if box == "Done":
        if space - box_space >= 0:
            print(f"{space - box_space} Cubic meters left.")

    if box_space - space >= 0:
        print(f"No more free space! You need {box_space - space} Cubic meters more.")

