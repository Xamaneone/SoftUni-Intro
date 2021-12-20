def read_matrix():
    (rows, columns) = map(int, input().split(", "))
    matrix = []
    for row_index in range(rows):
        row = list(map(int, input().split(" ")))
        matrix.append(row)
    return matrix

def get_column_sums(matrix):
    rows_count = len(matrix)
    columns_count = len(matrix[0])

    sums = []
    for column_index in range(columns_count):
        column_sum = 0
        for row_index in range(rows_count):
            column_sum += matrix[row_index][column_index]
        sums.append(column_sum)
    return sums

def print_result(values):
    [print(x) for x in values]

matrix = read_matrix()
result = get_column_sums(matrix)
print_result(result)