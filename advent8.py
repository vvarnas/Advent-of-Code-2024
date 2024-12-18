from itertools import combinations
import math

with open(r"/input8") as file:
    raw_data = file.read().split("\n")
raw_data.pop()

test_data = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

data = test_data.split("\n")
data = raw_data
y_range = len(data)
x_range = len(data[0])
antennas = set()
for i in range(x_range):
    for j in range(y_range):
        if data[j][i] !='.':
            antennas.add(data[j][i])

#Part 1
freqs = set()
for antenna in antennas:
    coords_x = []
    for i in range(x_range):
        for j in range(y_range):
            if data[j][i] == antenna:
                coords_x.append((i, j))
    pairs_x = list(combinations(coords_x, 2))
    for pair in pairs_x:
        x1, y1 = pair[0]
        x2, y2 = pair[1]

        dx = x2 - x1
        dy = y2 - y1

        antinode_1 = (x2 + dx, y2 + dy)
        antinode_2 = (x1 - dx, y1 - dy)
        if 0 <= antinode_1[0] < x_range and 0 <= antinode_1[1] < y_range:
            freqs.add(antinode_1)
        if 0 <= antinode_2[0] < x_range and 0 <= antinode_2[1] < y_range:
            freqs.add(antinode_2)
print(f"Total number of antinodes: {len(freqs)}")

#Part 2
freqs = set()
for antenna in antennas:
    coords_x = []
    for i in range(x_range):
        for j in range(y_range):
            if data[j][i] == antenna:
                coords_x.append((i, j))
    pairs_x = list(combinations(coords_x, 2))
    for pair in pairs_x:
        x1, y1 = pair[0]
        x2, y2 = pair[1]

        dx = x2 - x1
        dy = y2 - y1

        freqs.add((x1, y1))
        freqs.add((x2, y2))
        
        antinode_1 = (x2 + dx, y2 + dy)
        antinode_2 = (x1 - dx, y1 - dy)

        while 0 <= antinode_1[0] < x_range and 0 <= antinode_1[1] < y_range:
            freqs.add(antinode_1)
            antinode_1 = (antinode_1[0] + dx, antinode_1[1] + dy)

        while 0 <= antinode_2[0] < x_range and 0 <= antinode_2[1] < y_range:
            freqs.add(antinode_2)
            antinode_2 = (antinode_2[0] - dx, antinode_2[1] - dy)
print(f"Total number of antinodes: {len(freqs)}")
