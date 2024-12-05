# To find the crosses we'll start by finding the top line (M S / S M / M M / S S) and the check the rest of the pattern.

# Read in a list of lines and remove the blank one at the end
input = [x for x in open('input.txt').read().split('\n') if len(x) > 0]
# input = [x for x in open('example2.txt').read().split('\n') if len(x) > 0]


total = 0

for line_count, line in enumerate(input[:-2]):
    for n, char in enumerate(line):
        if char == "M" and n < len(line)-2 and line_count < len(input)-2:
            if line[n+2] == "S" and input[line_count + 1][n+1] == "A" and input[line_count + 2][n] == "M" and input[line_count + 2][n+2] == "S":
                total += 1
            elif line[n+2] == "M" and input[line_count + 1][n+1] == "A" and input[line_count + 2][n] == "S" and input[line_count + 2][n+2] == "S":
                total += 1
        elif char == "S" and n < len(line)-2 and line_count < len(input)-2:
            if line[n+2] == "M" and input[line_count + 1][n+1] == "A" and input[line_count + 2][n] == "S" and input[line_count + 2][n+2] == "M":
                total += 1
            elif line[n+2] == "S" and input[line_count + 1][n+1] == "A" and input[line_count + 2][n] == "M" and input[line_count + 2][n+2] == "M":
                total += 1

print(f"Total {total}")


