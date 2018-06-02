from strategy import *
from copy import deepcopy
class GameState:
    def __init__(self, is_p1_turn: bool) -> None:
        value = int(input("Choose your starting number."))
        self.value = value
        self.is_p1_turn = is_p1_turn
       
    def __str__(self):
        """
        For every move, the following string is presented to represent the
        current state of the game.
        """
        
        return "\n" + "The value is:" + str(self.value) + "\n"
    
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
        
        possible_moves = []
        possibilities = 1
        while possibilities**2 <= self.value:
            possible_moves.append(possibilities**2)
            possibilities = possibilities + 1
        possibilities = 1
        self.possible_moves = possible_moves
        return possible_moves
    
    def is_valid_move(self, move_to_make: int) -> bool:
        """Checks if the move in question is a valid move.
        >>>is_valid_move(1)
        True
        >>>is_valid_move(6)
        False
        """

        if move_to_make in self.get_possible_moves():
            
            return True
        else:
            return False
        
    def make_move(self, move: int):
        """Changes the turn and updates the current value of the state in the 
        Subtract Square game.
        """
        

        if self.is_p1_turn == True:
            self.is_p1_turn = False
        else:
            self.is_p1_turn = True
            
        newState = deepcopy(self)
        newState.value = self.value - move
        return newState