# For each line in the input we're going to start in include mode - including matches - 
# until we get to a don't, then set the include to false. That will toggle as we go along.
# We read in each line as a string, find the position of the next do / don't, and then if in
# include mode we'll multiple them and add to total. Thereafter trim off that part of string that we've
# checked and repeat.



import re

input = [x for x in open("input.txt").read().split("\n")]
# input = [x for x in open("example2.txt").read().split("\n")]

regex = r"mul\((\d+)\,(\d+)\)"
regex_dodont = r"do\(\)|don't\(\)"

total = 0
include = True

for line in input:

    while loc := re.search(regex_dodont, line):

        if include:
            matches = re.findall(regex, line[:loc.span()[0]])
            for m in matches:
                total += int(m[0]) * int(m[1])

        line = line[loc.span()[1]:]
        include = False if loc.group(0) == "don't()" else True

    if include:
        matches = re.findall(regex, line)
        for m in matches:
            total += int(m[0]) * int(m[1])

print(f"Total: {total}")

