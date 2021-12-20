def read_matrix():
    (rows, columns) = map(int, input().split(" "))
    matrix = []
    for r in range(rows):
        row = input().split(" ")
        matrix.append(row)
    return matrix, rows, columns

def subsqares_count(matrix,subsquare, rows, columns):
    count = 0
    for r in range(rows - (subsquare - 1)):
        for c in range(columns - (subsquare - 1)):
            data = set()
            for r2 in range(0, subsquare):
                for c2 in range(0, subsquare):
                    data.add(matrix[r + r2][c + c2])
            if len(data) == 1:
                count += 1
    return count
matrix, rows, columns = read_matrix()
subsquare = 2
print(subsqares_count(matrix, subsquare, rows, columns))


