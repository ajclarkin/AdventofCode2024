from aocd import submit
from collections import Counter


input = [int(x) for x in open("input.txt").read().split()]

left = input[::2]
right = input[1::2]

right_cnt = Counter(right)
total = 0

for l in left:
    total += l * right_cnt[l]


print(f"Total = {total}")
submit(total, part="b", day=1)
