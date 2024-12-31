from collections import defaultdict, deque
from itertools import product

# input = [x for x in open("example2.txt").read().split("\n") if len(x) > 0]
input = [x for x in open("input.txt").read().split("\n") if len(x) > 0]

grid = dict()
for rownum, row in enumerate(input):
    for colnum, char in enumerate(row):
        grid[(rownum, colnum)] = char

rowmax = len(row)
colmax = len(input)
perimeter = defaultdict(set)

plots = dict()
seen = set()
queue = deque()
corner_count = defaultdict(int)


def GetNeighbours(point, current):
    r, c = point
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    neighbours = []

    for dR, dC in directions:
        new_r, new_c = r + dR, c + dC
        if 0 <= new_r < rowmax and 0 <= new_c < colmax:
            if grid[(new_r, new_c)] == current:
                neighbours.append((new_r, new_c))

    return neighbours


# Added this because otherwise missing internal corners which are only a perimeter on the diagonal
# It returns the diagonals of the current cell which are a different crop.
def GetDiagonalNeighbours(point, current):
    r, c = point
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    neighbours = []

    for dR, dC in directions:
        new_r, new_c = r + dR, c + dC
        if 0 <= new_r < rowmax and 0 <= new_c < colmax:
            if grid[(new_r, new_c)] != current:
                neighbours.append((new_r, new_c))

    return neighbours



def CheckCorners(perimeter_point, all_plot_points):
    count = 0
    r, c = perimeter_point
    diagonals = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    for dR, dC in diagonals:
        new_r, new_c = r + dR, c + dC

        # check for convex corners - for each diagonal check to see that the two shoulder cells are not same crop
        if ((r + dR, c) not in grid or (r + dR, c) not in all_plot_points) and ((r, c + dC) not in grid or (r, c + dC) not in all_plot_points):
            count += 1

        # check for concave corners - diagonal if not current crop and both shoulders are current crop
        if ((r + dR, c) in all_plot_points ) and ((r, c + dC) in all_plot_points) and (new_r, new_c) not in all_plot_points:
            count += 1
    return count


for r, c in product(range(rowmax), range(colmax)):
    if (r, c) in seen:
        continue
    plots[(r, c)] = {(r, c)}
    queue.append((r, c))
    current_letter = grid[(r, c)]

    while queue:
        q = queue.popleft()
        seen.add(q)

        neighbours = GetNeighbours(q, current_letter)
        diag_neighbours = GetDiagonalNeighbours(q, current_letter)

        if len(neighbours) < 4 or len(diag_neighbours) > 0:
            perimeter[(r, c)].add(q)

        for n in neighbours:
            if n in seen:
                continue

            plots[(r, c)].add(n)
            seen.add(n)
            queue.append(n)


# At this point we have populated perimeter with the locations of each perimeter square for each garden patch
# plots and perimeter are both dicts with keys equal to the first cell in each area. Plots contains all the cells
# in the area and perimeter contains all the perimeter cells.

# Now check each of these to identify if it is a corner.
for plot in perimeter:
    for p in perimeter[plot]:
        corner_count[plot] += CheckCorners(p, plots[plot])

total = 0
for p in plots:
    total += len(plots[p]) * corner_count[p]
print(f"Final count: {total}")
