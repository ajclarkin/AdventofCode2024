input = [x for x in open('input.txt').read().split('\n')]
# input = [x for x in open('example2.txt').read().split('\n')]

# Make a dict containing the (row, col) of each punctuation mark
grid = dict()
list_x = list()

for rownum, row in enumerate(input):
    for colnum, char in enumerate(row):
        grid[(rownum, colnum)] = char
        if char == "X":
            list_x.append((rownum, colnum))

print(list_x)

# row, col
dirs = {
    "U": (-1, 0),
    "UR": (-1, 1),
    "R": (0, 1),
    "DR": (1, 1),
    "D": (1, 0),
    "DL": (1, -1),
    "L": (0, -1),
    "UL": (-1, -1),
}

total = 0
x_to_check = list_x[0]
for x_to_check in list_x:
    def AddDirection(current, direction, multiples):
        cur_r, cur_c = current
        add_r, add_c = direction
        
        new_position = (cur_r + add_r * multiples, cur_c + add_c * multiples)
        if new_position not in grid.keys():
            # This is a total fudge! This is what to do if the new point is not in the grid
            return(0, 0)
        else:
            return new_position


    for d in dirs.values():
        if (
            grid[AddDirection(x_to_check, d, 1)] == 'M' and
            grid[AddDirection(x_to_check, d, 2)] == 'A' and
            grid[AddDirection(x_to_check, d, 3)] == 'S'

        ):
            # print(f"yes, found at {x_to_check}")
            total += 1

print(f"Total: {total}")
