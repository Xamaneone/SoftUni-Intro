def read_matrix():
    square_matrix = int(input())
    matrix = []
    for line in range(square_matrix):
        row = list(map(int, input().split(" ")))
        matrix.append(row)
    return matrix

def diagonal_calculator(matrix, primary=False):
    sum = 0
    if primary:
        for row in range(len(matrix[0])):
            column = row
            sum += matrix[row][column]

    else:
        for row in range(-1 ,-(len(matrix[0])) - 1, -1):
            column = abs(row) - 1
            sum += matrix[row][column]
    return sum

def print_result(primary, secondary):
    print(abs(primary - secondary))



matrix = read_matrix()
primary_diagonal = diagonal_calculator(matrix, True)
secondary_diagonal = diagonal_calculator(matrix)
print_result(primary_diagonal, secondary_diagonal)

