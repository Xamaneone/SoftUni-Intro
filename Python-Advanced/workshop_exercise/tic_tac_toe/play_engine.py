from tic_tac_toe import setup
from tic_tac_toe.helpers import position_mapper


def is_row_winner(player):
    for row_number in range(len(setup.board)):
        if setup.board[row_number][0] == setup.board[row_number][1] == setup.board[row_number][2]:
            if setup.board[row_number][1] != " ":
                return True
    return False

def is_col_winner():
    for col_number in range(len(setup.board)):
        if setup.board[0][col_number] == setup.board[1][col_number] == setup.board[2][col_number]:
            if setup.board[1][col_number] != " ":
                return True
    return False

def is_diagonal_winner():
    if setup.board[0][0] == setup.board[1][1] == setup.board[2][2] or setup.board[2][0] == setup.board[1][1] == setup.board[0][2]:
        if setup.board[1][1] != ' ':
            return True
    return False


def has_won(player):
    if is_row_winner(player) or is_col_winner() or is_diagonal_winner():
        return True
    return False


def out_of_moves(board):
    for move in board:
        for spot in move:
            if spot == " ":
                return False
    return True


def draw_board(board):
    print()
    for row in range(len(board)):
        print(f"| {' | '.join(board[row])} |")

def position_available(board, selected_pos):
    row_num, col_num = position_mapper[selected_pos]
    current_element = board[row_num][col_num]
    if not current_element == " ":
        return False
    return True


def play_turn(board, sign, selected_pos):
    if is_position_valid(selected_pos):
        selected_pos = int(selected_pos)
        if position_available(board, selected_pos):
            row_num, col_num = position_mapper[selected_pos]
            board[row_num][col_num] = sign
            draw_board(board)
    else:
        current_selected_position = input(f"Please, insert a valid position from the free ones")
        while not current_selected_position.isdigit() and not is_position_valid(current_selected_position):
            current_selected_position = input("Please, insert a valid position from the free ones")
        current_selected_position = int(current_selected_position)
        play_turn(board, sign, current_selected_position)



def is_position_valid(pos):
    if str(pos).isdigit():
        return 0 < int(pos) < 10


def play(turns_counter):
    current_selected_position = input(f"{setup.player_names[turns_counter % 2]}, select a position from [0-9]: ")
    while not current_selected_position.isdigit() and is_position_valid(current_selected_position):
        current_selected_position = input(f"{setup.player_names[turns_counter % 2]}, select a valid position [0-9]: ")
    play_turn(setup.board, setup.player_signs[turns_counter % 2], current_selected_position)
    if has_won(turns_counter):
        print(f"{setup.player_names[turns_counter % 2]} is a winner! Congrats!")
        return
    if out_of_moves(setup.board):
        print(f"Tie! Everyone is a winner!")
        return
    play(turns_counter + 1)



