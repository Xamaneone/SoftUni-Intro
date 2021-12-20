def square_matrix_generator(size):
    return [input().split(", ") for _ in range(size)]

def find_diagonal(matrix ,first_diagonal=True):
    if first_diagonal:
        return [matrix[index][index] for index in range(size)]
    else:
        return [matrix[index][size - 1 - index] for index in range(size)]


size = int(input())
matrix = square_matrix_generator(size)
first_diagonal = find_diagonal(matrix)
second_diagonal = find_diagonal(matrix, False)
print(f"First diagonal: {', '.join(first_diagonal)}. Sum: {sum(map(int, first_diagonal))}")
print(f"Second diagonal: {', '.join(second_diagonal)}. Sum: {sum(map(int, second_diagonal))}")