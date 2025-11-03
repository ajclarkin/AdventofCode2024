lines = [x for x in open('example1.txt').read().split('\n') if x != '']
grid = dict()

for rownum, row in enumerate(lines):
    for colnum, char in enumerate(row):
        grid[(rownum, colnum)] = char
        if char == "S": start = (rownum, colnum)
        if char == "E": end = (rownum, colnum)

rowmax = len(row)
colmax = len(lines)
total = 0

print(lines)
print(start, end, rowmax, colmax)
print(grid)
