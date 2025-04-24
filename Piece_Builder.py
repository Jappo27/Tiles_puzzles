from collections import defaultdict

def Build(Block):
    Dict = defaultdict(list)
    for i in range(len(Block)):
        Dict[i] = [Block[i][0], Block[i][1], Block[i][2], Block[i][3]]
    return Dict
