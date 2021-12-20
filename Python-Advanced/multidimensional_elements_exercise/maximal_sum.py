def read_matrix():
    (rows, columns) = map(int, input().split(" "))
    matrix = []
    for r in range(rows):
        row = list(map(str, input().split(" ")))
        matrix.append(row)
    return matrix, rows, columns

def maximal_sum(matrix,subsquare, rows, columns):
    best_sum = -9999999
    best_result = []
    for r in range(rows - (subsquare - 1)):
        for c in range(columns - (subsquare - 1)):
            current_data = []
            current_sum = 0
            for r2 in range(0, subsquare):
                temp = []
                for c2 in range(0, subsquare):
                    index = matrix[r + r2][c + c2]
                    if index.isdigit():
                        current_sum += int(index)
                    temp.append(index)
                current_data.append(temp)
            if best_sum < current_sum:
                best_sum = current_sum
                best_result = current_data
    return best_result, best_sum

def print_result(matrix, sum):
    print(f"Sum = {sum}")
    for row in matrix:
        for el in row:
            print(el, end=" ")
        print()


matrix, rows, columns = read_matrix()
subsquare = 3
matrix_result, max_sum = maximal_sum(matrix, subsquare, rows, columns)
print_result(matrix_result, max_sum)
