#which lines correspond to what

def load_map(path):
    f = open(path + '.txt', "r")
    data = f.read()
    f.close()
    data = data.split("\n")
    game_map = []

    for row in data:
        game_map.append([int(i) for i in row])
    return game_map

def print_2d_array(arr):
    for row in arr:
        for col in row:
            print(col, end="")
        print()
