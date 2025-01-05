import re
import math
robots = list()

# input = [x for x in open('example.txt').read().split('\n') if len(x) > 0]
# colmax = 11
# rowmax = 7

input = [x for x in open('input.txt').read().split('\n') if len(x) > 0]
colmax = 101
rowmax = 103

cycles = 100 
quadrants = [0,0,0,0]

for i in input:
    c, r, dc, dr = map(int, re.findall("-?\d+", i))
    robots.append([c, r, (dc, dr)])


for r in robots:
    print(r[0], r[1], r[2])
    r[0] = (r[0] + cycles * r[2][0]) % colmax
    r[1] = (r[1] + cycles * r[2][1]) % rowmax

    if r[0] == colmax // 2 or r[1] == rowmax // 2:
        continue

    if r[0] < colmax//2 and r[1] < rowmax//2: quadrants[0] += 1
    if r[0] < colmax//2 and r[1] > rowmax//2: quadrants[2] += 1
    if r[0] > colmax//2 and r[1] < rowmax//2: quadrants[1] += 1
    if r[0] > colmax//2 and r[1] > rowmax//2: quadrants[3] += 1



print(quadrants)
print(math.prod(quadrants))
