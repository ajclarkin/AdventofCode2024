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
perimeter_count = defaultdict(int)

plots = dict()
seen = set()
queue = deque()


def GetNeighbours(point, current):
    r, c = point
    directions = [(1,0), (-1,0), (0,1), (0,-1)]  
    neighbours = []
    
    for dR, dC in directions:
        new_r, new_c = r + dR, c + dC
        if 0 <= new_r < rowmax and 0 <= new_c < colmax:
            if grid[(new_r, new_c)] == current:
                neighbours.append((new_r, new_c))
    
    return neighbours


for r, c in  product(range(rowmax), range(colmax)):
    if (r, c) in seen:
        continue
    plots[(r,c)] = {(r,c)}
    queue.append((r,c))
    current_letter = grid[(r,c)]

    while(queue):
        q = queue.popleft()
        seen.add(q)


        neighbours = GetNeighbours(q, current_letter)

        if len(neighbours) < 4:
           perimeter_count[(r,c)] += 4 - len(neighbours) 

        for n in neighbours:
            if n in seen:
                continue

            plots[(r,c)].add(n)
            seen.add(n)
            queue.append(n)
                
total = 0
for d in plots:
    print(f"Plot {d} has area {len(plots[d])} and perimeter {perimeter_count[d]}")
    total += len(plots[d]) * perimeter_count[d]
print(f"total: {total}")
