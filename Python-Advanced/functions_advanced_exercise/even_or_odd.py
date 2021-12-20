def even_odd(*args):
    if "even" in args:
        return list(filter(lambda x: x % 2 == 0, [args[i] for i in range(len(args) - 1)]))
    return list(filter(lambda x: x % 2 == 1, [args[i] for i in range(len(args) - 1)]))



# print(even_odd(1, 2, 3, 4, 5, 6, "even"))
# print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
