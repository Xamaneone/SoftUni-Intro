def field_generator(n):
    field = [list(map(str, input().split(" "))) for _ in range(n)]
    return field


def find_player_coordinates(field):
    for row in range(len(field)):
        for col in range(len(field)):
            if field[row][col] == "P":
                return row, col


def in_range(field, current_row, current_col):
    if 0 <= current_row < len(field) and 0 <= current_col < len(field) and field[current_row][current_col] != "X":
        return True
    return False

def is_win(coins):
    if coins >= 100:
        return True
    return False

def play(field, player_row, player_col, available_moves):
    coins = 0
    path = []
    while coins < 100:
        direction = input()
        current_row = player_row + available_moves[direction][0]
        current_col = player_col + available_moves[direction][1]
        if not in_range(field, current_row, current_col):
            break
        coins += int(field[current_row][current_col])
        field[player_row][player_col] = "0"
        field[current_row][current_col] = "P"
        player_row, player_col = current_row, current_col
        path.append([current_row, current_col])
    if is_win(coins):
        print(f"You won! You've collected {coins} coins.")
    else:
        coins /= 2
        coins = int(coins)
        print(f"Game over! You've collected {coins} coins.")
    print(f"Your path:")
    for line in path:
        print(f"{line}")




available_moves = {
    "up": (-1, +0),
    "down": (+1, +0),
    "left": (+0, -1),
    "right": (+0, +1),
}


field_size = int(input())

field = field_generator(field_size)

player_row, player_col = find_player_coordinates(field)

play(field, player_row, player_col, available_moves)

