from collections import deque

#TODO I M NOT WORKING


BUNNY = "B"
PLAYER = "P"

def read_input():
    rows, columns = [int(x) for x in input().split(' ')]
    lair = []
    for _ in range(rows):
        lair.append(list(input()))
    directions = input()
    return lair, directions

lair, directions = read_input()

def get_bunnies(lair):
    bunnies = []
    for row_index in range(len(lair)):
        for column_index in range(len(lair[0])):
            if lair[row_index][column_index] == BUNNY:
                bunnies.append((row_index, column_index))
    return bunnies

def get_player(lair):
    for row_index in range(len(lair)):
        for column_index in range(len(lair[0])):
            if lair[row_index][column_index] == PLAYER:
                return (row_index, column_index)


def get_next_move(player, dir):
    dir_deltas = {
        'U': (-1, 0),
        'D': (+1, 0),
        'L': (0, -1),
        'R': (0, +1),
    }
    (row_index, column_index) = player
    (row_delta, column_delta) = dir_deltas[dir]

    return row_index + row_delta, column_index + column_delta


def in_range(value, max_value):
    return 0 <= value < max_value


def spread_bunnies(lair, bunnies):
    rows_count = len(lair)
    columns_count = len(lair[0])
    for _ in range(len(bunnies)):
        bunny = bunnies.popleft()
        next_bunnies = [
            get_next_move(bunny, dir) for dir in 'UDLR'
        ]
        next_bunnies = [
            (row_index, column_index)
            for (row_index, column_index) in next_bunnies
            if in_range(row_index, columns_count) \
            and in_range(column_index, columns_count) \
            and lair[row_index][column_index] != BUNNY
        ]
        for (row_index, col_index) in next_bunnies:
            lair[row_index][col_index] = BUNNY
            bunnies.append((row_index, col_index))


def is_win(lair, player):
    (row_index, column_index) = player
    return not in_range(row_index, len(lair)) or not in_range(column_index, len(lair[0]))

def is_loss(lair, player):
    pass

def print_result(lair, row_index, column_index, is_win):
    [print(''.join(row)) for row in lair]
    if is_win:
        print(f"won: {row_index} {column_index}")
    else:
        print(f"dead: {row_index} {column_index}")

def play_game(lair, bunnies, player, directions):
    row_index, column_index = player
    for dir in directions:
        spread_bunnies(lair, bunnies)
        next_row_index, next_column_index = get_next_move((row_index, column_index), dir)
        if is_win(lair, (next_row_index, next_column_index)):
            lair[next_row_index, next_column_index] = PLAYER
            print_result(lair, row_index, next_column_index, is_win=True)
        elif is_loss(lair, (next_row_index, next_column_index)):
            print_result(lair, row_index, next_column_index, is_win=False)

        lair[row_index][column_index] = '.'
        lair[next_row_index][next_column_index] = PLAYER
        row_index, column_index = next_row_index, next_column_index



player = get_player(lair)
bunnies = get_bunnies(lair)
player = get_player(lair)


bunnies_queue = deque(bunnies)
play_game(lair, bunnies_queue, player, directions)
#
# print_result(lair, (0, 0), False)
# print(bunnies_queue)