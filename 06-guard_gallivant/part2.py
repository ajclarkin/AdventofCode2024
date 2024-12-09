from itertools import cycle
import itertools

input = [x for x in open('input.txt').read().split('\n')]
# input = [x for x in open('example.txt').read().split('\n')]

# Make a dict containing the (row, col) of each punctuation mark
# grid = dict()

space = set()
obstacle = set()
# This time we need to know unique positions and the direction at the time.
unique_positions = set()

for rownum, row in enumerate(input):
    for colnum, char in enumerate(row):
        if char == '#':
            obstacle.add((rownum, colnum))
        else:
            space.add((rownum, colnum))

        if char == "^":
            startpos = (rownum, colnum)


# row, col
dirs = {
    "U": (-1, 0),
    "R": (0, 1),
    "D": (1, 0),
    "L": (0, -1),
}
rowlen = len(input[0])
collen = len(input)
valid_positions = 0
search_space = len(space)

# We need to add an external loop to repeat the path-following multiple times, starting from the same position,
# and reseting the direction list each time.

test_space = space.copy()

while test_space:
    # Add a countdown timer
    print(search_space)
    search_space -= 1

    test_obstacle = obstacle.copy()
    testing = test_space.pop()
    test_obstacle.add(testing)

    curpos = startpos
    unique_positions = set()
    dirlist = itertools.cycle(["U", "R", "D", "L"])
    curdir = next(dirlist)
    while 0 <= curpos[0] < rowlen and 0<= curpos[1] < collen:
        # If we are in a position we've been at before and moving in the same direction then we've found a loop.
        if ((curpos, curdir)) in unique_positions:
            valid_positions += 1
            break
        else:
            unique_positions.add((curpos, curdir))

        nextpos = (curpos[0] + dirs[curdir][0], curpos[1] + dirs[curdir][1])

        if nextpos in test_obstacle:
            curdir = next(dirlist)
        else:
            curpos = nextpos
print(f"Total valid obstacles: {valid_positions}")
