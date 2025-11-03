# input = [int(x) for x in open('input.txt').read() if x != '\n']
# input = [int(x) for x in open('example.txt').read() if x != '\n']
input = [int(x) for x in '1313165'] # 169
# input = [int(x) for x in '2333133121414131499'] # 6204

blocks = list()
blanks = False



# Store the sizes of each blank space in order
blank_sizes = input[1::2]

# Expand the list as it is at the beginning
for n, char in enumerate(input):
    blocks += ['.' if blanks else n//2] * char
    blanks = False if blanks else True

def FindNBlankBlock(n):
    # Find the start of the nth block of blanks
    # Return the position of the start of the block we want, or false if a viable block not found
    # print(f"Entered function looking for block {n}")
    block_count = 0
    prev_char = ''
    for cnt, char in enumerate(blocks):
        if char == '.' and prev_char != '.':
            block_count += 1
        if block_count == n:
            return cnt
        prev_char = char
    else:
        return False


def NewFindBlankBlock(n):
    # Given n, find the nth blank block
    # For the first blank block n will be 1

    prev_index = -1
    block_count = 0

    while '.' in blocks[prev_index+1:] and block_count < n:
        blank_loc = blocks.index('.')
        if blank_loc - 1 != prev_index:
            block_count += 1
        prev_index = blank_loc
    return blank_loc


# print(blocks)
l = len(input)-1
while l >= 0:
    # print("Blanks:", blank_sizes)
    block_len = input[l]
    block_value = l//2

    # print(f"need a block length of {block_len} and a value of {block_value}")

    for n, size in enumerate(blank_sizes):
        if size >= block_len:
            # n contains the index of the location to move to
            # print(f"Blank block starts at {FindNBlankBlock(n+1)}") 
            # blank_start = FindNBlankBlock(n+1)
            blank_start = NewFindBlankBlock(n+1)
            if blank_start is False:
                continue
            # print(f"I seem to think the blank should start at {blank_start}")

            if block_value not in blocks:
                print(f"Weird - {block_value} not in blocks")
                continue
            curr_block_pos = blocks.index(block_value)
            if blank_start < curr_block_pos:
                while block_value in blocks:
                    blocks[blocks.index(block_value)] = '.'
                for j in range(block_len):
                    blocks[blank_start + j] = block_value

                blank_sizes[n] -= block_len
                if 0 in blank_sizes:
                    blank_sizes.remove(0)

                while blocks[-1] == '.':
                    blocks.pop()

                break

    l -= 2

    # print(blocks)

total = 0
for n, v in enumerate(blocks): 
    if type(v) is int:
        total += n * v
    else:
        continue

print(f"Total: {total}")

# 2806880027587 is too low
# 2807131241302 is wrong
# 4857456025086 wrong
