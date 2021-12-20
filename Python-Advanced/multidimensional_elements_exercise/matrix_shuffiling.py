def read_matrix():
    (rows, columns) = map(int, input().split(" "))
    matrix = []
    for r in range(rows):
        row = list(map(str, input().split(" ")))
        matrix.append(row)
    return matrix, rows, columns


def command_legit(command):
    if command.startswith("swap") and len(command.split(" ")) == 5:
        return True
    return False

def swap_function(matrix, command, rows, columns):
    command = command.replace("swap ", "")
    (fi, fc, si, sc) = map(int ,command.split(" "))
    if rows > int(fi) and columns > int(fc) and rows > int(si) and columns > int(sc):
        new_matrix = matrix
        matrix = []
        first_item, second_item = new_matrix[fi][fc], new_matrix[si][sc]
        column = 0
        for line in new_matrix:
            data = []
            row = 0
            for word in line:
                if row == fc and column == fi:
                    data.append(second_item)
                elif row == sc and column == si:
                    data.append(first_item)
                else:
                    data.append(word)
                row += 1
            column += 1
            matrix.append(data)
        return matrix
    return False

matrix, rows, columns = read_matrix()

command = str(input())

while command != "END":
    if not command_legit(command):
        print("Invalid input!")
    else:
        new_matrix = swap_function(matrix, command, rows, columns)
        if new_matrix != False:
            matrix = new_matrix
            for row in matrix:
                print(*row)
        else:
            print("Invalid input!")


    command = str(input())