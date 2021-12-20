def ascii_to_char(row):
    return [(chr(97 + row) + chr(97 + row + col) + chr(97 + row)) for col in range(0, columns)]

def palindromes_generator(rows, columns):
    matrix = [ascii_to_char(row) for row in range(rows)]
    for row in matrix:
        print(*row)


rows, columns = map(int, input().split(" "))
palindromes_generator(rows, columns)