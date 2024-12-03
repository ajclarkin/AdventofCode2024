import re


input = [x for x in open("input.txt").read().split("\n")]
# input = [x for x in open("example.txt").read().split("\n")]

regex = r"mul\((\d+)\,(\d+)\)"
total = 0

for line in input:
    matches = re.findall(regex, line)
    
    for m in matches:
        total += int(m[0]) * int(m[1])


print(f"Total: {total}")
