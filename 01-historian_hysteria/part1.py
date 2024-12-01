from aocd import submit


input = [int(x) for x in open("input.txt").read().split()]

left = input[::2]
right = input[1::2]

left.sort()
right.sort()

total = 0

for v1, v2 in zip(left, right):
    total += abs(v2 - v1)

print(f"Total = {total}")
submit(total)
