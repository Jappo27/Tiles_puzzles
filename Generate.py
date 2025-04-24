from Process import slide_left, slide_right, slide_top, slide_bot, check_legal_moves
from copy import deepcopy
import time
start = time.time()

def find_keys_for_value(Piece_Type, value):
    for key, val in Piece_Type.items():
        if val == value:
            return key

def Board_string(Piece_Type, Blocks, board_dimensions):
    blank_board = [["x"] * board_dimensions[0] for i in range(board_dimensions[1])]

    for i in range(len(Blocks)):
        p_tpye_ID = find_keys_for_value(Piece_Type, [Blocks[i][0], Blocks[i][1]])

        for j in range(Blocks[i][3], Blocks[i][3] + Blocks[i][1]):
            for k in range(Blocks[i][2], Blocks[i][2] + Blocks[i][0]):
                blank_board[j][k] = p_tpye_ID

    board_string = ''.join(str(cell) for row in blank_board for cell in row)
    return board_string

def genTree(Pieces, start, Goal, Piece_Type, board_dimensions):
    moves = {
        0: (slide_left),
        1: (slide_right),
        2: (slide_top),
        3: (slide_bot)
            }
    all_Boards = []
    board = (Pieces, [(Pieces[0][2], Pieces[0][3], Pieces[0][2], Pieces[0][3])])
    queue = [board]

    g_str = Board_string(Piece_Type, Goal, board_dimensions)

    valid = True
    for goal in list(Goal.values()):
        if goal not in list(queue[0][0].values()):
            valid = False
            break
                            
    if  valid:
        return queue[0][1]
    
    while queue and time.time() < start + 60:
        board_b = queue.pop(0)
        b_str = Board_string(Piece_Type, board_b[0], board_dimensions)
        if g_str == b_str:
            return board_b[1]
        elif b_str not in all_Boards:
            all_Boards.append(b_str)
            legal_moves = check_legal_moves(board_b[0], board_dimensions)
            l_m = []

            for i in range(len(legal_moves)):
                for j in range(len(legal_moves[i])):
                    if legal_moves[i][j] == 0:
                        l_m.append(([i, j]))

            for m in l_m:
                i, j  = m[0], m[1]
                board_b_clone = deepcopy(board_b)
                move = [board_b_clone[0][i][2], board_b_clone[0][i][3], 0, 0]
                temp_p = moves[j](i, board_b_clone[0])
                        
                move[2], move[3] = temp_p[i][2], temp_p[i][3]
                board_b_clone[1].append(tuple(move))
            
                queue.append((temp_p, board_b_clone[1]))

    return -1
