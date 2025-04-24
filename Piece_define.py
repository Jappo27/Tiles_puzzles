from collections import defaultdict

def p_ID_Builder(Pieces, Piece_Type = defaultdict(list)):
    for key, value in Pieces.items():
        # Check if value[0] and value[1] are not in new_d
        if not any(value[0:2] == existing_value[0:2] for existing_value in Piece_Type.values()):
            # If not, append to new_d at last key + 1
            new_key = max(Piece_Type.keys()) + 1 if Piece_Type else 0
            Piece_Type[new_key] = value[0:2]
    return Piece_Type
