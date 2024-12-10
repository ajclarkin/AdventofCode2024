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

# Use a copy of equations for further testing
equations_copy = equations.copy()



total = 0

# This time I have turned this into a function so that I can call it twice, and there's
# a parameter to vary the operations which are being tested.

def CheckEquations(operations):
    global total
    for e in equations:
        target, parts = e
        parts_copy = parts.copy
        ops_to_try = itertools.product(operations, repeat=len(parts)-1)

        for combo in ops_to_try:
            value = parts[0] 
            for i, op in enumerate(combo):
                if op == 'a':
                    value = value + parts[i+1]
                elif op == 'm':
                    value = value * parts[i+1]
                elif op == 'c':
                    value = int(str(value) + str(parts[i+1]))

                if value > target:
                    break
                
            if value == target:
                equations_copy.remove(e)
                total += target
                break

# First run through - find the true equations that we did in part 1
CheckEquations('am')

# Sync the lists again - the copy is the one we have removed the true equations from so
# that they don#t need to be checked again.
equations = equations_copy.copy()

# Next - for the remaining equations check them again but this time with concatenate as an option. 
CheckEquations('amc')


print(f"Final total: {total}")
