"""Phrase Puzzler: functions"""

# Phrase Puzzler constants

# Name of file containing puzzles
DATA_FILE = 'puzzles_small.txt'

# Letter values
CONSONANT_POINTS = 1
VOWEL_PRICE = 1
CONSONANT_BONUS = 2

# Players' names
PLAYER_ONE = 'Player One'
PLAYER_TWO = 'Player Two'

# Menu options - includes letter types
CONSONANT = 'C'
VOWEL = 'V'
SOLVE = 'S'
QUIT = 'Q'


# Define your functions here.

def is_win(puzzle: str, view: str) -> bool:
    """Return True if and only if puzzle is the same as view.

    >>> is_win('banana', 'banana')
    True
    >>> is_win('apple', 'a^^le')
    False
    """
    return puzzle == view

def game_over(puzzle: str, view: str, menu: str) -> bool:
    """Return True if and only if puzzle is the same as view or the menu option
    is QUIT.
    
    >>> game_over('banana', 'banana', QUIT)
    True
    >>> game_over('apple', 'banana', QUIT)
    True
    """
    return (puzzle == view) or (menu == QUIT)

def bonus_letter(puzzle: str, view: str, letter: str) -> bool:
    """Return True if and only if the letter is not in the view but is in the
    puzzle.
    
    >>> bonus_letter('banana', 'apple', 'b')
    True
    >>> bonus_letter('banana', 'apple', 'a')
    False
    """
    return (letter not in view) and (letter in puzzle)

def update_letter_view(puzzle: str, view: str, index: int, letter: str) -> str:
    """Return the letter if the character matches the index of the puzzle, else 
    return the character of index in view.
    
    >>> update_letter_view('banana', 'apple', 2, 'n')
    n
    >>> update_letter_view('banana', 'apple', 2, 'a')
    p
    """
    if letter == puzzle[index]:
        return letter
    else:
        return view[index]

#occurence is the number of times the letter has appeared in the puzzle
#let_type is whether the letter is a CONSONANT or a VOWEL
def calculate_score(current_score: int, occurence: int, let_type: str) -> int:
    """Return the score by adding CONSONANT_POINTS for every occurence of the
    letter that is a consonant and subtract VOWEL_POINTS for every occurence of 
    a letter that is a vowel.
    
    >>> calculate_score(0, 5, CONSONANT)
    5
    >>> calculate_score(4, 2, VOWEL)
    2
    """
    if let_type == CONSONANT:
        return current_score + occurence
    else:
        return current_score - occurence

#current_player is the player who is playing the game: PLAYER_ONE or PLAYER_TWO
#puzzle_occurence is the number of occurences in the puzzle of the letter
#this letter was last chosen by the current_player
def next_player(current_player: str, puzzle_occurence: int) -> str:
    """Return the next player as current_player if and only if the 
    puzzle_occurence is greater than 0, otherwise return the other player.
    
    >>> next_player(PLAYER_ONE, 3)
    PLAYER_ONE
    >>> next_player(PLAYER_ONE, 0)
    PLAYER_TWO
    """
    if puzzle_occurence > 0:
        return current_player
    else:
        if current_player == PLAYER_ONE:
            return PLAYER_TWO
        else:
            return PLAYER_ONE
