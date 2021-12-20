def is_valid_explosion(row, col, explosion_row, explostion_col):
    if 0 <= row < matrix_size and 0 <= col < matrix_size:
        if not matrix[row][col] <= 0:
            if explosion_row - 1 <= row < explosion_row + 2  and explosion_col - 1 <= col < explosion_col + 2:
                return True
    return False

matrix_size = int(input())

matrix = []

for row in range(matrix_size):
    matrix.append(list(map(int, input().split(" "))))

explosion_coordinates = input().split(" ")

while explosion_coordinates:
    temp = explosion_coordinates.pop(0).split(",")
    (explosion_row, explosion_col) = int(temp[0]), int(temp[1])
    explosion_dmg = matrix[explosion_row][explosion_col]
    if not explosion_dmg <= 0:
        for current_row in range(matrix_size):
            for current_col in range(matrix_size):
                if is_valid_explosion(current_row, current_col, explosion_row, explosion_col):
                    matrix[current_row][current_col] -= explosion_dmg


alive_cells = 0
sum = 0
for row in matrix:
    for cell in row:
        if cell > 0:
            alive_cells += 1
            sum += cell

print(f"Alive cells: {alive_cells}")
print(f"Sum: {sum}")

for row in matrix:
    print(*row)