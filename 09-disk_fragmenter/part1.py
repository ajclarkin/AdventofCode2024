
input = [int(x) for x in open('input.txt').read() if x != '\n']
# input = [int(x) for x in open('example.txt').read() if x != '\n']
# input = [int(x) for x in '12345'] 

blocks = list()
blanks = False

for n, char in enumerate(input):
    blocks += ['.' if blanks else n//2] * char

    blanks = False if blanks else True



n = 0
while (n < len(blocks)-1):
    if blocks[n] == '.' :
        newchar = ''
        while type(newchar) is not int:
            newchar = blocks.pop()
        else:
            blocks[n] = newchar
    n += 1

total = 0
for n, v in enumerate(blocks): 
    if type(v) is int:
        total += n * v
    else:
        break

print(f"Total: {total}")
