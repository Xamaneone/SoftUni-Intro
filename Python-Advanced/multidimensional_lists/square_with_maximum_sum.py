def read_matrix():
    (rows, columns) = map(int, input().split(", "))
    matrix = []
    for row_index in range(rows):
        row = list(map(int, input().split(", ")))
        matrix.append(row)
    return matrix

def get_sum_of_submatrix(matrix, row_index, column_index, size):
    the_sum = 0
    for r in range(row_index, row_index + size):
        for c in range(column_index, column_index + size):
            the_sum += matrix[r][c]
    return the_sum



matrix = read_matrix()

submatrix_size = 2
best_row_index = 0
best_column_index = 0
best_sum = get_sum_of_submatrix(matrix, 0, 0, submatrix_size)

for row_index in range(len(matrix) - submatrix_size + 1):
    for col_index in range(len(matrix[row_index]) - submatrix_size + 1):
        current_sum = get_sum_of_submatrix(matrix, row_index, col_index, submatrix_size)
        if best_sum < current_sum:
            best_sum = current_sum
            best_row_index = row_index
            best_column_index = col_index


for r in range(best_row_index, best_row_index + submatrix_size):
    row = []
    for c in range(best_column_index, best_column_index + submatrix_size):
        row.append(matrix[r][c])
    print(" ".join(str(x) for x in row))

print(best_sum)

