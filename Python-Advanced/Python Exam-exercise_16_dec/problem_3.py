def get_magic_triangle(number):
    magic_triangle = [[1], [1, 1]]
    number -= 2
    while number:
        number -= 1
        magic_triangle.append([1])
        for n in range(1, len(magic_triangle[-2])):
            magic_triangle[-1].append(magic_triangle[-2][n - 1] + magic_triangle[-2][n])
        magic_triangle[-1].append(1)
    return magic_triangle





# print(get_magic_triangle(5))