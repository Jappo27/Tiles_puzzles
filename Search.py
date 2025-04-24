from collections import defaultdict
from File_data_sift import get_values
from Piece_Builder import Build
from Piece_define import p_ID_Builder
from Build_Board import build_board
from Blocks import gen_Pieces
from Generate import genTree
import time
import sys

files = {}

def queue_check(queue):
    if queue == -1:        
        print(f"{queue}")    
    elif len(queue) == 1:        
        print(f"{queue[0][0]} {queue[0][1]} {queue[0][2]} {queue[0][3]}")    
    else:        
        queue = queue[1:]
        for i in range(len(queue)):
            print(f"{queue[i][0]} {queue[i][1]} {queue[i][2]} {queue[i][3]}")


files[sys.argv[1]] = sys.argv[2]
for key in files.keys():
        start = time.time()
        board_dimensions, Blocks, Goal_Blocks = get_values(key, files[key])
        
        pieces = gen_Pieces(Blocks)
        Goal = Build(Goal_Blocks)
        Pieces = Build(Blocks)

        Goal_Board = build_board(defaultdict(list), Goal_Blocks, board_dimensions)
        Board = build_board(defaultdict(list), Blocks, board_dimensions)
        Piece_Type = p_ID_Builder(Pieces)

        queue = genTree(Pieces, start, Goal, Piece_Type, board_dimensions)
        queue_check(queue)
