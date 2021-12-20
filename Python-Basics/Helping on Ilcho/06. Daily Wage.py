columns = int(input())
positions = int(input())
strawberries = 0
blueberries = 0
for i in range(1, columns + 1):
    for o in range(1, positions + 1):
        if i % 2 == 1:
            strawberries += 1
        else:
            if not o % 3 == 0:
                blueberries += 1
strawberries = strawberries * 3.50
blueberries = blueberries * 5
sum = strawberries + blueberries
print(f"Total: {sum * 0.80:.2f} lv.")