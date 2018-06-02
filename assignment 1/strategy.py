from typing import Any

# TODO: Adjust the type annotation as needed.
def interactive_strategy(game: Any) -> Any:
    """
    Return a move for game through interactively asking the user for input.
    """
    print("adfkladjflkdas")
    move = input("Enter a move: ")
    return game.str_to_move(move)

def long_game_strategy(game: Any) -> Any:
    """
    Chooses the smallest possible move.
    """
    move = 1
    return game.str_to_move(move)
