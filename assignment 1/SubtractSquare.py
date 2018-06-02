from strategy import *
from current_state import *

class SubtractSquare:
    """
    Choose a positive whole number and keep subtracting squares of various
    numbers if the result is not a negative number.
    """
    def __init__(self, is_p1_turn: bool) -> None:
        """
        Initialize the game with instantiating with another class
        and determine Player 1.
        """
        self.is_p1_turn = is_p1_turn
        current_state = GameState(True)
        self.value = current_state.value
        self.current_state = current_state
    
    def is_over(self, current_state) -> bool:
        """
        This method determines when the game is over.
        """
        return current_state.value == 0
    
    def get_instructions(self) -> str: 
        """
        Returns the instruction of the game as follows.
        """
        return ("Player 1" + 
        " chooses a positive whole number and Player 2 subtract"
        + " it by a squared number such as 1, 4, 9, etc. Then the players" +
        " alternate subtracting number until the result cannot be positive.")
    
    def str_to_move(self, move: str) -> int:
        """
        Receives the input and then converts it to integer.
        """
        if move:
            return int(move)
        else:
            pass
    
    def is_winner(self, players) -> None:
        """
        Depending on if the game is over and who's turn it ends on, this method
        declares if the player in question is the winner.
        """
        if self.current_state.value == 0:
            if players == "p1":
                if self.current_state.is_p1_turn == True and self.current_state\
                .value == 0:
                    return False
                else:
                    return True
            elif players == "p2":
                if self.current_state.is_p1_turn == True and self.current_state\
                .value == 0:
                    return True
                else:
                    return False
        else:
            return False
            
