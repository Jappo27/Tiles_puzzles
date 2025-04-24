def build_board(dictionary, Blocks, board_dimensions):
    Board = [["x"] * board_dimensions[0] for _ in range(board_dimensions[1])]

    for i in range(len(Blocks)):
        for j in range(Blocks[i][3], Blocks[i][3] + Blocks[i][1]):
            for k in range(Blocks[i][2], Blocks[i][2] + Blocks[i][0]):
                Board[j][k] = i
    
    for i in range(len(Board)): 
        dictionary[i] = Board[i]
    return dictionary
