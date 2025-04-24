class block:
    def __init__(self, hoz_len, ver_len, x_pos, y_pos):
        self.hoz_len = hoz_len
        self.ver_len = ver_len
        self.x_pos = x_pos
        self.y_pos = y_pos

def gen_Pieces(Blocks):
    pieces = []
    for i in range(len(Blocks)):
        pieces.append(block(Blocks[i][0], Blocks[i][1], Blocks[i][2], Blocks[i][3]))
    return pieces
