input = [x for x in open('example.txt'). read().split('\n\n')]
# input = [x for x in open('input.txt'). read().split('\n\n')]
lines = input[0].split('\n')
movements = list(input[1].replace('\n', ''))

grid = dict()

for rownum, row in enumerate(lines):
    for colnum, char in enumerate(row):
        grid[(rownum, colnum)] = char
        if char == "@":
            curpos = (rownum, colnum)

rowmax = len(row)
colmax = len(lines)
total = 0

dirs = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}



def PrintGrid(grid):
    for i in range(rowmax):
        for j in range(colmax):
            print(grid[(i, j)], end='')
        print()


def CanMove(symbol, movefrom, dir):
    r, c = movefrom
    dr, dc = dirs[dir]
    new_r = r + dr
    new_c = c + dc

    if grid[(new_r, new_c)] == '#':
        return False

    elif grid[(new_r, new_c)] == '.':
        grid[(new_r, new_c)] = symbol
        return True

    else:
        if CanMove('O', (new_r, new_c), dir):
            grid[(new_r, new_c)] = symbol
            return True



for move in movements:
    r, c = curpos

    if CanMove('@', curpos, move):
        grid[curpos] = '.'
        curpos = (r + dirs[move][0], c + dirs[move][1])

    PrintGrid(grid)     
locs = [k for k,v in grid.items() if v == 'O']
values = [100 * k[0] + k[1] for k in locs]

print(f"Total: {sum(values)}")

