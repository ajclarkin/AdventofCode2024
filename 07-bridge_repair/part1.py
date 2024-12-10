import itertools
import re

# lines = [x for x in open('example.txt').read().split('\n') if x != '']
lines = [x for x in open('input.txt').read().split('\n') if x != '']

# Read the data so we have a list of elements, each of which is a tuple of final value
# and list of numbers to test, eg (190, [10, 19])
equations = list()
for l in lines:
    nums = [int(x) for x in re.findall(r'\d+', l)]
    equations.append((nums[0], nums[1:]))



total = 0
for e in equations:
    target, parts = e
    ops_to_try = itertools.product('am', repeat=len(parts)-1)

    for combo in ops_to_try:
        value = parts[0] 
        for i, op in enumerate(combo):
            if op == 'a':
                value = value + parts[i+1]
            elif op == 'm':
                value = value * parts[i+1]

            if value > target:
                break
            
        if value == target:
            print(f"Met target {target} with combo {combo}")
            total += target
            break

print(f"Final total: {total}")
