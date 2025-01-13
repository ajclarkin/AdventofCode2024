# input = [x for x in open('edge4.txt'). read().split('\n\n')]
input = [x for x in open('input.txt'). read().split('\n\n')]

lines = input[0].split('\n')
movements = list(input[1].replace('\n', ''))

# Update lines to show new symbols
newlines = []
for k, l in enumerate(lines):
    l = l.replace('#', '##')
    l = l.replace('O', '[]')
    l = l.replace('.', '..')
    l = l.replace('@', '@.')
    newlines.append(l)

grid = dict()

for rownum, row in enumerate(newlines):
    for colnum, char in enumerate(row):
        grid[(rownum, colnum)] = char
        if char == "@":
            curpos = (rownum, colnum)

colmax = len(newlines[0])
rowmax = len(newlines)
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
        if dir in ['<', '>'] or symbol == '@':
            grid[(new_r, new_c)] = symbol
        else:
            changes[(new_r, new_c)] = symbol
            will_move.add((r, c))
        return True


    elif grid[(new_r, new_c)] == ']' and dir == '<':
        if CanMove('[', (new_r, new_c-1), dir):
            changes[(new_r, new_c-1)] = ']'
            changes[(new_r, new_c)] = symbol
            return True 

    elif grid[(new_r, new_c)] == '[' and dir == '>':
        if CanMove(']', (new_r, new_c+1), dir):
            changes[(new_r, new_c+1)] = '['
            changes[(new_r, new_c)] = symbol
            return True 

        # must be [ or ] going up or down
    else:
        if grid[(new_r, new_c)] == '[' and CanMove('[', (new_r, new_c), dir) and CanMove(']', (new_r, new_c+1), dir):
            changes[(new_r, new_c)] = symbol
            will_move.add((r, c))
            return True

        if grid[(new_r, new_c)] == ']' and CanMove(']', (new_r, new_c), dir) and CanMove('[', (new_r, new_c-1), dir):
            changes[(new_r, new_c)] = symbol
            will_move.add((r, c))
            return True


for move in movements:
    changes = dict()
    will_move = set()
    
    r, c = curpos

    if CanMove('@', curpos, move):
        changes[curpos] = '.'
        curpos = (r + dirs[move][0], c + dirs[move][1])

        # update grid with changes
        for k, v in changes.items():
            grid[k] = v
                
        # Some pieces will have moved but won't be replaced by another piece - identify them and change to .
        # (For example, if the left side of a box is pushed up the right side also goes. The old left side will be replaced by whatever pushed but the right 
        # will need a . added)
        new_blanks = [w for w in will_move if w not in changes.keys()]
        for b in new_blanks:
            grid[b] = '.'

locs = [k for k,v in grid.items() if v == '[']
values = [100 * k[0] + k[1] for k in locs]
print(f"Total: {sum(values)}")


