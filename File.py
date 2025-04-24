import ast

def list_files_and_goals(directory_path):
    data_list = []
    data_dict = {}
    with open(directory_path, 'r') as f:
        for line in f:
            data_list.append(ast.literal_eval(line))

    data_dict[data_list[len(data_list)-1:][0][0]] = data_list[len(data_list)-1:][0][1]
    data_list = data_list[:-1]

    for i in range(len(data_list)):
        data_dict[data_list[i][0][0]] = data_list[i][0][1]

    return data_dict

Paths = ["Csv_files\easy_puzzles.csv", "Csv_files\medium_puzzles.csv", "Puzzles\hardCsv_files\hard_puzzles.csv"]
Path = ["easy", "medium", "hard"]
n = 0
files = list_files_and_goals(Paths[n])
