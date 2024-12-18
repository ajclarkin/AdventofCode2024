input = [x for x in open('input.txt').read().split('\n') if len(x) > 0]
# input = [x for x in open('example.txt').read().split('\n') if len(x) > 0]

zeros = dict() 
nines = set()
loc = dict()

rowmax = len(input[0])
colmax = len(input)

def FindNeighbours(loc):
    neighbours = list()
    r, c = loc
    for dR, dC in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_r, new_c = r + dR, c + dC
        if 0 <= new_r < rowmax and 0<= new_c < colmax:
            neighbours.append((new_r, new_c))
    return neighbours


# Populate loc dictionary with grid values
for rownum, row in enumerate(input):
    for colnum, char in enumerate(row):
        char = int(char)
        loc[(rownum, colnum)] = char

        if char == 0:
            zeros[(rownum, colnum)] = set()
        elif char == 9:
            nines.add((rownum, colnum))


def FollowPaths(point):
    global zeros
    neighbours = FindNeighbours(point) 
    neighbours = [x for x in neighbours if loc[point] - loc[x] == 1]
    if len(neighbours) == 0:
        if loc[point] == 0:
            global nine
            zeros[point].add(nine)
    else:
        for n in neighbours:
            FollowPaths(n)

for nine in nines:
    FollowPaths(nine)

total = 0
for v in zeros.values():
    total += len(v)

print(f"Total: {total}")

