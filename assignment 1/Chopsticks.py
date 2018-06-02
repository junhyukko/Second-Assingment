from strategy import *
from current_state import *
class Chopsticks:

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
        current_state = GameStateChop(True)
        self.current_state = current_state
    
    def is_over(self, current_state) -> bool:
        """
        This method determines when the game is over.
        """
        return (current_state.p1left ==5 and current_state.p1right == 5) 
    
    def get_instructions(self) -> str: 
        """
        Returns the instruction of the game as follows.
        """
        return ("Player 1" + 
        " chooses a hand and then player two also chooses a hand. Go team."
        )
    
    def str_to_move(self, move: str) -> int:
        """
        Receives the input and then converts it to integer.
        """
        if move:
            return move
        else:
            pass
    
    def is_winner(self, players) -> None:
        """
        Depending on if the game is over and who's turn it ends on, this method
        declares if the player in question is the winner.
        """
        if players =='p1':
            return self.current_state.p2left ==5 and self.current_state.p2right == 5
        else:
            return (self.current_state.p1left ==5 and selfcurrent_state.p1right == 5)
            
class GameStateChop:
    def __init__(self, is_p1_turn: bool) -> None:
        
        self.p1left = 1
        self.p1right = 1
        self.p2left = 1
        self.p2right = 1
        
        self.is_p1_turn = is_p1_turn
       
    def __str__(self):
        """
        For every move, the following string is presented to represent the
        current state of the game.
        """
        
        return "workinprogress"
    
    def get_current_player_name(self) -> str:
        """
        Determines who the current player is.
        >>>get_current_player_name()
        p1
        """
        
        if self.is_p1_turn == True:
            return 'p1'
        else:
            return 'p2'
    
    def get_possible_moves(self) -> list:
        """
        A list of possible moves are made to be presented to the players on what
        the valid moves can be.
        """
        
        possible_moves = ['left,left', 'left,right', 'right,left', 'right,right']
        return possible_moves
    
    def is_valid_move(self, move_to_make: str) -> bool:
        """Checks if the move in question is a valid move.
        >>>is_valid_move(1)
        True
        >>>is_valid_move(6)
        False
        """

        if move_to_make == 'left,left' or move_to_make == 'right,left':
            if self.is_p1_turn:
                return not self.p2left == 5
            else:
                return not self.p1left == 5
        else:
            if self.is_p1_turn:
                return not self.p2right == 5
            else:
                return not self.p1right == 5
        
    def make_move(self, move: str):
        """Changes the turn and updates the current value of the state in the 
        Subtract Square game.
        """
        
        newState = deepcopy(self)
        if move == 'left,left':
            if self.is_p1_turn:
                newState.p2left = newState.p2left + self.p1left 
            else:
                newState.p1left = newState.p1left + self.p2left 
        elif(move == 'right,left'):
            if self.is_p1_turn:
                newState.p2left = newState.p2left + self.p1reft 
            else:
                newState.p1left = newState.p1left + self.p2reft
        elif(move == 'left,right'):#right,right
            
            if self.is_p1_turn:
                newState.p2right = newState.p2right + self.p10left 
            else:
                newState.p1right = newState.p1right + self.p2left 
        else:
            if self.is_p1_turn:
                newState.p2right = newState.p2right + self.p1right 
            else:
                newState.p1right = newState.p1right + self.p2right            
       
        
        return newState