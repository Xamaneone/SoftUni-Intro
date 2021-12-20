def read_matrix():
    rows_count = int(input())
    return [input().split(", ")for _ in range(rows_count)]

matrix = read_matrix()
print([int(x) for row in matrix for x in row])