def get_values(file, goal_file):
    Blocks = []     
    with open(file) as board_file:
        lines = board_file.readlines()
        board_dimensions = [int(num) for num in lines[0].split()]
        for line in lines[1:]:
            Blocks.append([int(num) for num in line.split()])

    with open(goal_file) as goal_file:
        lines = goal_file.readlines()
        Goal_board = [[int(num) for num in line.split()] for line in lines]
        
    return board_dimensions, Blocks, Goal_board
