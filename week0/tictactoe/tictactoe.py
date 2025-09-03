"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0

    for row in board:
        x_count += row.count(X)
        o_count += row.count(O)

    if x_count > o_count:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_moves = set()

    for row_index, row in enumerate(board):
        for column_index, cell in enumerate(row):
            if cell is EMPTY:
                possible_moves.add((row_index, column_index))

    return possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    current_player = player(board)
    new_board = deepcopy(board)
    row, col = action

    if board[row][col] is not EMPTY or row > 2 or row < 0 or col > 2 or col < 0:
        raise Exception
    else:
        new_board[row][col] = current_player

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for current_player in (X, O):
        # Check rows
        for row in board:
            if row == [current_player] * 3:
                return current_player

        # Check columns
        for col in range(3):
            column = [board[row][col] for row in range(3)]
            if column == [current_player] * 3:
                return current_player
        
        # Check diagonals
        if [board[i][i] for i in range(0, 3)] == [current_player] * 3:
            return current_player

        elif [board[i][~i] for i in range(0, 3)] == [current_player] * 3:
            return current_player
        
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    win = winner(board)
    empty_count = 0
    for row in board:
        empty_count += row.count(EMPTY)

    if win is not None or empty_count is 0:
        return True
    else:
        return False
    

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)

    if win is X:
        return 1
    elif win is O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """ 
    if terminal(board) is True:
        return None
    
    current_player = player(board)

    if current_player is X:
        return max_value(board)[1]
    else:
        return min_value(board)[1]


def max_value(board):
    optimal_move = ()
    if terminal(board):
        return utility(board), optimal_move
    else:
        v = -math.inf
        for action in actions(board):
            min_val = min_value(result(board, action))[0]
            if min_val > v:
                v = min_val
                optimal_move = action
        return v, optimal_move


def min_value(board):
    optimal_move = ()
    if terminal(board):
        return utility(board), optimal_move
    else:
        v = 5
        for action in actions(board):
            max_val = max_value(result(board, action))[0]
            if max_val < v:
                v = max_val
                optimal_move = action
        return v, optimal_move

