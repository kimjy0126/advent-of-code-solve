from aocd import data
from aocd.models import Puzzle

def is_diagonal(node):
    if abs(node[0]-node[2]) == abs(node[1] - node[3]):
        return True
    else:
        return False
puzzle = Puzzle(year=2021, day=5)
res = 0

data_string = puzzle.input_data

# data_string = """0,9 -> 5,9
# 8,0 -> 0,8
# 9,4 -> 3,4
# 2,2 -> 2,1
# 7,0 -> 7,4
# 6,4 -> 2,0
# 0,9 -> 2,9
# 3,4 -> 1,4
# 0,0 -> 8,8
# 5,5 -> 8,2"""

is_part2 = True
data = data_string.split("\n")
numbers_s = data_string.replace("->", "").replace(",", " ").replace("\n", " ").replace("  ", " ").split(" ")
numbers = [int(x) for x in numbers_s]
map_size = max(numbers) + 1
ocean = [ [0]*map_size for i in range(map_size)]
max_overlap = 0

valid_nodes_x = []
valid_nodes_y = []
for node in data:
    p2p = node.split("->")
    x1 = int(p2p[0].strip().split(",")[0])
    y1 = int(p2p[0].strip().split(",")[1])
    x2 = int(p2p[1].strip().split(",")[0])
    y2 = int(p2p[1].strip().split(",")[1])
    _node = (x1,y1,x2,y2)
    if x1 == x2:
        valid_nodes_x.append(_node)
        for i in range(min(y1,y2), max(y1,y2)+1):
            ocean[i][x1] += 1
    elif y1 == y2:
        valid_nodes_y.append(_node)
        for i in range(min(x1,x2), max(x1,x2)+1):
            ocean[y1][i] += 1
    elif is_diagonal(_node):
        if is_part2 == True:
            direction_x = 1 if x2 > x1 else -1
            direction_y = 1 if y2 > y1 else -1
            _x, _y = x1 , y1
            for i in range(abs(x1 - x2) + 1):
                ocean[_y][_x] += 1
                _x += 1 * direction_x
                _y += 1* direction_y
    else:
        pass

score = sum([sum(map(lambda x: x>1, o)) for o in ocean])
print(score)
