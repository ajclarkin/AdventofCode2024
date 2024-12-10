import itertools

input = [x for x in open('input.txt').read().split('\n') if x != '']
# input = [x for x in open('example.txt').read().split('\n')]
antenna = dict()
antinodes = set()

for rownum, row in enumerate(input):
    for colnum, char in enumerate(row):
        if char != '.':
            if char in antenna:
                antenna[char].append((rownum, colnum))
            else:
                antenna[char] = [(rownum, colnum)]

rowmax = len(input[0])
colmax = len(input)

# Find all the valid locations for antinodes
for ant_type in antenna:
    pairs = itertools.combinations(antenna[ant_type], 2)
    for p in pairs:
        point0, point1 = p
        dR = point1[0] - point0[0]
        dC = point1[1] - point0[1]
        if (0 <= (point0[0] - dR) < rowmax) and (0 <= (point0[1] - dC) < colmax):
            antinodes.add((point0[0] - dR, point0[1] - dC))
        if (0 <= (point1[0] + dR) < rowmax) and (0 <= (point1[1] + dC) < colmax):
            antinodes.add((point1[0] + dR, point1[1] + dC))
print(f"Total {len(antinodes)}")

