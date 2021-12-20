DEFAULT_ROWS_COUNT = 6
DEFAULT_COLUMNS_COUNT = 7
DEFAULT_WIN_CONDITION_COUNT = 4




def apply_player_choice(board, column_index, player):
    row_index = get_lowest_free_row_index(board, column_index)
    board[row_index][column_index] = player
    return board


def has_win_condition(board, player):
    rows_count = len(board)
    for row_index in range(rows_count):
        columns_count = len(board[row_index])
        for column_index in range(columns_count):
            if has_win_condition_from_position(board, row_index, column_index, player):
                return True
    return False

def has_win_condition_from_position(board, row_index, column_index, player, win_condition_count=DEFAULT_WIN_CONDITION_COUNT):
    rows_count = len(board)
    columns_count = len(board[0])
    end_column_index = column_index + win_condition_count
    end_row_index = row_index + win_condition_count
    horizontal_values = [in_range(c, columns_count) and board[row_index][c] == player
                         for c in range(column_index, end_column_index)]
    vertical_values = [in_range(r, rows_count) and board[r][row_index] == player
                       for r in range(row_index, end_row_index)]
    left_diagonal = [in_range()]
    right_diagonal = [in_range()]


    return all(horizontal_values) or all(vertical_values)




def create_board(rows_count=DEFAULT_ROWS_COUNT, columns_count=DEFAULT_COLUMNS_COUNT):
    return [[0] * columns_count for _ in range(rows_count)]

def in_range(value, max_value):
    return 0 <= value < max_value

def get_player_choice(player):
    print(f"Player {player}, please choose a column")
    return int(input()) - 1


def get_lowest_free_row_index(board, column_index):
    rows_count = len(board)
    for row_index in range(rows_count -1, -1, -1):
        if board[row_index][column_index] == 0:
            return row_index
    return None

def play(board, player=1):
    print_board(board)
    while True:
        player_choice = get_player_choice(player)
        apply_player_choice(board, player_choice, player)
        print_board(board)
        if has_win_condition(board, player):
            print_winner_message(player)
            break
        player = 2 if player == 1 else 1


def print_board(board):
    for row in board:
        print(row)


def print_winner_message(player):
    print(f"The winner is player {player}!")





board = create_board()

play(board)



