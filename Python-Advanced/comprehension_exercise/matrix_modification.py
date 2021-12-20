



def matrix_generator(number):
    return [list(map(int, input().split(" "))) for _ in range(number)]

def matrix_editor(act, row, col, value, matrix, matrix_size):
    (row, col) = int(row), int(col)
    value = [int(value)]
    if act == "Add":
        for current_col in range(matrix_size):
            for current_row in range(matrix_size):
                if current_row == row and current_col == col:
                    matrix[current_row][current_col] += value.pop()
                    return matrix
    else:
        for current_col in range(matrix_size):
            for current_row in range(matrix_size):
                if current_row == row and current_col == col:
                    matrix[current_row][current_col] -= value.pop()
                    return matrix
    if value:
        print("Invalid coordinates")
        return matrix

matrix_size = int(input())
matrix = matrix_generator(matrix_size)


command = input()
while command != "END":
    act, row, col, value = command.split(" ")
    matrix = matrix_editor(act, row, col, value, matrix, matrix_size)
    command = input()


for row in matrix:
    print(*row)