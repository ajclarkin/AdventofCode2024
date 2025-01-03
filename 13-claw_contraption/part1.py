import re
import numpy as np

# input = [x for x in open('example.txt').read(). split('\n\n') if len(x) > 0]
input = [x for x in open('input.txt').read(). split('\n\n') if len(x) > 0]


total = 0

for i in input:
    nums = [int(x) for x in re.findall("\d+", i)]
    coefs = np.array([[nums[0], nums[2]], [nums[1], nums[3]]])
    values = np.array(nums[4:])

    try:
        solution = np.linalg.solve(coefs, values)
        if all(list(map(lambda x: np.isclose(x, round(x)) , solution))):
            total += 3 * solution[0] + solution[1]
    except np.linalg.LinAlgError:
        pass

print(f"Final total: {int(total)}")

