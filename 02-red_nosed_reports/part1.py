# Classic AoC - this should be simple data extraction.
# input = [x for x in open("example.txt").read().split('\n')]
input = [x for x in open("input.txt").read().split('\n')]
lines = [[int(d) for d in i.split(' ')] for i in input if i != '']


def CheckDifferences(line, ascending = True):
    for l in range(len(line) -1):
        if (1 <= (line[l+1] - line[l]) <= 3) and ascending:
            pass
        elif (1 <= (line[l] - line[l+1]) <= 3) and not ascending:
            pass
        else:
            break
    else:
        return 1
    return 0


total = 0

for line in lines:
    if line == sorted(line):
        total += CheckDifferences(line)
    elif line == sorted(line, reverse=True):
        total += CheckDifferences(line, ascending=False)


print(f"Final total: {total}")
