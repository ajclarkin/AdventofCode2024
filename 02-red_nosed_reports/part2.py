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
    expanded_line = list()
    expanded_line.append(line)

    for n, letter in enumerate(line):
        line_copy = line.copy()
        line_copy.pop(n)
        expanded_line.append(line_copy)

    found_safe_option = 1
    for line_variant in expanded_line:
        # first check order
        if line_variant  == sorted(line_variant) and CheckDifferences(line_variant):
            break
        elif line_variant   == sorted(line_variant, reverse=True) and CheckDifferences(line_variant, ascending=False):
            break
        
        # then check differences
        # then break
    else:
        found_safe_option = 0

    if found_safe_option:
        total += 1


print(f"Total safe rows: {total}")


