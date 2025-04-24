from Build_Board import build_board
from collections import defaultdict

def printBoard(Pieces):
    for i in range(len(Pieces)):
        print(Pieces[i])

#piece =  hoz_len, ver_len, x_pos, y_pos

def check_left(Pieces, Board, n):
    if (Pieces[n][2] -1) < 0:
        return -1
    
    for j in range(Pieces[n][3], Pieces[n][3] + Pieces[n][1]):
        if  Board[j][Pieces[n][2] - 1] != "x":
            return -1
    return 0

def check_right(pieces, Board, n):
    if (pieces[n][2] + pieces[n][0] + 1) > len(Board[0]):
        return -1
    
    for j in range(pieces[n][3], pieces[n][3] + pieces[n][1]):
        if  Board[j][pieces[n][2] + pieces[n][0]] != "x":
            return -1
    return 0

def check_top(pieces, Board, n):
    if (pieces[n][3] - 1) < 0:
        return -1
    
    for j in range(pieces[n][2], pieces[n][2] + pieces[n][0]):
        if  Board[pieces[n][3] - 1][j] != "x":
            return -1
    return 0

def check_bot(pieces, Board, n):
    if (pieces[n][3] + pieces[n][1] + 1) > len(Board):
        return -1
    
    for j in range(pieces[n][2], pieces[n][2] + pieces[n][0]):
        if  Board[pieces[n][3] + pieces[n][1] ][j] != "x":
            return -1
    return 0

def add_legal(legal_move):
    for k in range(1, len(legal_move)):
        if legal_move[k] == 0:
            return 0
    return -1

def check_legal_moves(Pieces, board_dimensions):
    legal_moves = defaultdict(list)
    Board = build_board(defaultdict(list), Pieces, board_dimensions)

    for i in range(len(Pieces)):
        legal_move = []
        
        legal_move.append(check_left(Pieces, Board, i))
        legal_move.append(check_right(Pieces, Board, i)) 
        legal_move.append(check_top(Pieces, Board, i)) 
        legal_move.append(check_bot(Pieces, Board, i))
        legal_moves[i] = (legal_move)

    return legal_moves

def slide_left(n, pieces):

    #move one step left
    pieces[n][2] -= 1
    return pieces

def slide_right(n, pieces):

    # Move one step right
    pieces[n][2] += 1
    return pieces

def slide_top(n, pieces):

    # Move one upwards
    pieces[n][3] -= 1
    return pieces


def slide_bot(n, pieces):

    # Move the piece one step downwards
    pieces[n][3] += 1
    return pieces
