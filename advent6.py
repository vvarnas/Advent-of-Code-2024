from tqdm import tqdm

with open(r"/Users/varnas/Desktop/vscode/input6") as file:
    raw_data = [list(line) for line in file.read().strip().split("\n")]

sample = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""


sample_data = grid = [list(line) for line in sample.strip().split("\n")]

x_range = len(raw_data[0])  # Width of the grid
y_range = len(raw_data)    # Height of the grid

def initial_coords(data):
    x_range = len(data[0])  
    y_range = len(data)
    for i in range(y_range):
        row = data[i]
        for j in range(x_range):
            if row[j] == "^":
                x = j
                y = i
                return (x, y)  
        
initial_pos = initial_coords(raw_data)

x, y = initial_pos
#Part 1
print(initial_pos)
direction = 0
dd = [[0, -1], [1, 0], [0, 1], [-1, 0]]
real_visited = set()

while True:
    real_visited.add((x, y))
    new_x = x + dd[direction][0]
    new_y = y + dd[direction][1]
    
    if not (0 <= new_x < x_range and 0 <= new_y < y_range):
        break 
    
    if raw_data[new_y][new_x] == "#":
        direction = (direction + 1) % 4
    
    else:
        x, y = new_x, new_y

print(f"Unique visited loactions: {len(real_visited)}")

#Part 2
def loop_objects(O_x, O_y):
    data_copy = [row[:] for row in raw_data]  # Proper deep copy
    if data_copy[O_y][O_x] == "#":  # Fix indexing issue
        return False
    
    data_copy[O_y][O_x] = "#"  # Place obstacle
    x, y = initial_pos

    direction = 0
    dd = [[0, -1], [1, 0], [0, 1], [-1, 0]]
    visited = set()

    while True:
        if (x, y, direction) in visited:
            return True  # Loop detected
        visited.add((x, y, direction))
        new_x = x + dd[direction][0]
        new_y = y + dd[direction][1]
        
        if not (0 <= new_x < x_range and 0 <= new_y < y_range):
            return False 
        
        if data_copy[new_y][new_x] == "#":
            direction = (direction + 1) % 4
        else:
            x, y = new_x, new_y

loops = 0

for O_x, O_y in tqdm(real_visited):
    if (O_x, O_y) == initial_pos:
        continue
    if loop_objects(O_x, O_y):
        loops += 1

print(f"Number of objects inducing a loop: {loops}")