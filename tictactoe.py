"""
Tic Tac Toe Player
"""

from json.encoder import INFINITY
import math
import copy
from operator import truediv


X = "X"
O = "O"
EMPTY = None

gScenariosChecked = 0 #DEBUG

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
    #raise NotImplementedError
    #I need to check the board and count the number of X and 0 available
    #then return which turn's it is
    #Loop through a list of lists
    noOfX = 0
    noOfO = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                noOfX += 0
            if board[i][j] == X:
                noOfX += 1
            if board[i][j] == O:
                noOfO += 1
    
    #print("Number Of X {}, Number of 0s {}".format(noOfX,noOfO)) # DEBUG !!
    
    if noOfX > noOfO:
        return(O)
    if noOfO > noOfX:
        return(X)
    if noOfX == noOfO:
        return(X)

    #returnX


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # raise NotImplementedError
    # Create an empty set to store the actions
    possibleActions = set()
    # Loop through the board and check if empty
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                # print("Found empty position in {0},{1}".format(i,j))
                possibleActions.add((i,j))
    return(possibleActions)
    

def result(pBoard, pAction):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Do not modify the original board

    # Copy of the board
    lBoardCopy = copy.deepcopy(pBoard)
    #Get whose turns is it (Xs or 0s):
    locPlayer = player(lBoardCopy)
    
    #Check if action is valid (the cell should be empty)
    if (lBoardCopy[pAction[0]][pAction[1]] != None):
        raise Exception("Illegal Move!")
    lBoardCopy[pAction[0]][pAction[1]]=locPlayer
    #print(lBoardCopy)
    return(lBoardCopy)


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #raise NotImplementedError
    # Check rows:
    for i in range(3):
        #if (board[i][1] == board[i][2]) and (board[i][1] == board[i][2]) and (board[i][1] != None):
        if (board[i][0] == board[i][1] == board[i][2]) and  (board[i][1] != None):
            return(board[i][1])
    # Check columns:
    for j in range(3):
        #if (board[1][j] == board[2][j]) and (board[1][j] == board[2][j]) and (board[1][j] != None):
        if (board[0][j] == board[1][j] == board[2][j]) and (board[1][j] != None):
            return(board[1][j])
    # Check Diagonals:
    if (board[1][1]==board[0][0]==board[2][2]) and (board[1][1] != None):
        return(board[1][1])
    if (board[1][1]==board[0][2]==board[2][0]) and (board[1][1] != None):
        return(board[1][1])

    return(None)    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #raise NotImplementedError
    #return False
    #print("Checking it it is a terminal state") # DEBUG !!
    #print(board)
    # count the board and see if there are 3 in on a row
    ConsecutiveX = 0
    ConsecutiveO = 0
    NumberOfMoves = 0

    if winner(board) == "X":
        return(True)
    if winner(board) == "O":
        return(True)
    # Count the number of cells:
    for i in range(3):
        for j in range(3):
            if (board[i][j] != None):
                NumberOfMoves += 1
    if (NumberOfMoves == 9):
        return(True)
    
    # Else, not terminal
    return(False)



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    #raise NotImplementedError
    if winner(board) == X:
        return(1)
    elif winner(board) == O:
        return(-1)
    else:
        return(0)


def minValue(board):
    # 1st: verify if the game is over.
    # If it is terminal, should return None
    if terminal(board):
        return(utility(board))

    # It was not a terminal position
    # Therefore we have to review every possible action
    locValue = INFINITY

    # Loop through all possible actions:
    lActions = actions(board)
    #print("Possible Actions:")
    #print(lActions)

    # Take a deep copy of the board (we don't want to modify it)
    lBoardOriginal = copy.deepcopy(board)
    lBoardCopy = copy.deepcopy(board)

    # Evaluate each of the possible actions
    for action in lActions:
        #print('minValue, Action: ' + str(action))
        locValue = min(locValue,maxValue(result(lBoardCopy,action)))   
    return(locValue)


def maxValue(board):
    # 1st: verify if the game is over.
    # If it is terminal, should return None
    if terminal(board):
        return(utility(board))

    # It was not a terminal position
    # Therefore we have to review every possible action
    locV = -INFINITY

    # Loop through all possible actions:
    lActions = actions(board)

    # Take a deep copy of the board (we don't want to modify it)
    lBoardOriginal = copy.deepcopy(board)
    lBoardCopy = copy.deepcopy(board)

    # Evaluate each of the possible actions
    for action in lActions:
        #print('maxValue, Action: ' + str(action))
        
        # Evaluate the action
        locV=max(locV,minValue(result(lBoardCopy,action)))
    return(locV)



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    lBoardOriginal = copy.deepcopy(board)
    lBoardCopy = copy.deepcopy(board)

    # If it is terminal, return none
    if terminal(board):
        return(None)
    
    #lActions = actions(board)
    #for action in lActions:

    # Maximizing score
    #print("###MiniMax") # DEBUG
    if (player(board) == "X"):
        bestVal = -INFINITY
        lActions = actions(board)
        for action in lActions:
            print(action) # DEBUG

            k = minValue(result(lBoardCopy,action))

            if k > bestVal:
                bestVal = action
                best_move = action



    if (player(board) == "O"):
        bestVal = INFINITY
        lActions = actions(board)
        for action in lActions:
            #print('minimax action' + str(action)) # DEBUG

            k = maxValue(result(lBoardCopy,action))
            if (k < bestVal):
                bestVal = k
                best_move = action

    return best_move
