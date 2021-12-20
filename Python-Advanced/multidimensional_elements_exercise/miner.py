from collections import deque


def get_field(n):
    return [input().split(" ") for _ in range(n)]

def get_player(field):
    for row in range(len(field) - 1):
        for col in range(len(field[0]) - 1):
            if field[row][col] == "s":
                return row, col


def get_coals(field):
    coals = 0
    for row in range(len(field)):
        for col in range(len(field[0])):
            if field[row][col] == "c":
                coals += 1
    return coals


def in_range(value, max_value):
    return 0 <= value < max_value

def play(field, player_row, player_col, player_directions, possible_directions):
    max_value = len(field)
    game_over = False
    coals_collected = 0
    coals_remaining = get_coals(field)
    while True:
        if player_directions:
            row, col = possible_directions[player_directions.popleft()]
            current_row, current_col = player_row + row, player_col + col
            if in_range(current_row, max_value) and in_range(current_col, max_value):
                field[player_row][player_col] = "*"
                current_symbol = field[current_row][current_col]
                if current_symbol == "e":
                    game_over = True
                elif current_symbol == "c":
                    coals_collected += 1
                    coals_remaining -= 1
                player_row, player_col = current_row, current_col
                field[player_row][player_col] = "s"
        else:
            print(f"{coals_remaining} coals left. {player_row, player_col}")
            break
        if game_over:
            print(f"Game over! {player_row, player_col}")
            break
        if coals_remaining == 0:
            print(f"You collected all coals! {player_row, player_col}")
            break








possible_directions = {
    "up": (-1, +0),
    "down": (+1, +0),
    "left": (+0, -1),
    "right": (+0, +1),
}


n = int(input())

player_directions = deque(input().split(" "))

field = get_field(n)

player_row, player_col = get_player(field)

play(field, player_row, player_col, player_directions, possible_directions)

