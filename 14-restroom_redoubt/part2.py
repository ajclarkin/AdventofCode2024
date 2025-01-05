from collections import defaultdict
import re
robots = list()

inp = [x for x in open('input.txt').read().split('\n') if len(x) > 0]
for i in inp:
    c, r, dc, dr = map(int, re.findall("-?\d+", i))
    robots.append([c, r, (dc, dr)])


colmax = 101
rowmax = 103



# Function to view the actual layout to look for Christmas Trees
def ViewLayout(robots):
    positions = set()
    for r in robots:
        positions.add((r[0], r[1]))

    for row in range(rowmax):
        print('\n', end='')
        for col in range(colmax):
            if (col, row) in positions:
                print('#', end='')
            else:
                print('.', end='')
            


for lcv in range(10000):
    col_rows = defaultdict(set)
    for r in robots:
        r[0] = (r[0] + r[2][0]) % colmax
        r[1] = (r[1] + r[2][1]) % rowmax
    
        col_rows[r[0]].add(r[1])

    for c in col_rows:
        if len(col_rows[c]) > 30:
            input("Wait")
            ViewLayout(robots)
            print(lcv + 1)
            break
