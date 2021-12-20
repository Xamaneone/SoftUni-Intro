from tic_tac_toe.setup import setup
from tic_tac_toe.play_engine import play

if __name__ == "__main__":
    setup()
    play(0)
    new_game = input(f"Do you want to play a new game? y/n")
    while new_game.lower() == 'y':
        setup()
        play(0)
        new_game = input(f"Do you want to play a new game? y/n")
