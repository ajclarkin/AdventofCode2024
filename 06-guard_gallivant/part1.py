from itertools import cycle
import itertools

input = [x for x in open('input.txt').read().split('\n')]
# input = [x for x in open('example.txt').read().split('\n')]

# Make a dict containing the (row, col) of each punctuation mark
# grid = dict()

space = set()
obstacle = set()
unique_positions = set()

for rownum, row in enumerate(input):
    for colnum, char in enumerate(row):
        if char == '#':
            obstacle.add((rownum, colnum))
        else:
            space.add((rownum, colnum))

        if char == "^":
            curpos = (rownum, colnum)


# row, col
dirlist = itertools.cycle(["U", "R", "D", "L"])
dirs = {
    "U": (-1, 0),
    "R": (0, 1),
    "D": (1, 0),
    "L": (0, -1),
}
rowlen = len(input[0])
collen = len(input)

curdir = next(dirlist)
while 0 <= curpos[0] < rowlen and 0<= curpos[1] < collen:
    unique_positions.add(curpos)
    nextpos = (curpos[0] + dirs[curdir][0], curpos[1] + dirs[curdir][1])

    if nextpos in obstacle:
        curdir = next(dirlist)
    else:
        curpos = nextpos

print(f"Total positions: {len(unique_positions)}")
