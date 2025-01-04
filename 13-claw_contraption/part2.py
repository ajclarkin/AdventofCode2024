import re
import numpy as np

# input = [x for x in open('example.txt').read(). split('\n\n') if len(x) > 0]
input = [x for x in open('input.txt').read(). split('\n\n') if len(x) > 0]


total = 0
offset = 10000000000000

for i in input:
    nums = [int(x) for x in re.findall("\d+", i)]
    coefs = np.array([[nums[0], nums[2]], [nums[1], nums[3]]])
    values = np.array([x + offset for x in nums[4:]])

    try:
        solution = np.linalg.solve(coefs, values)
        if all(list(map(lambda x: np.isclose(x, round(x), rtol=1e-14) , solution))):
            total += 3 * solution[0] + solution[1]
            print(i)
            print(list(map(str, solution)))
    except np.linalg.LinAlgError:
        print("error")

print(f"Final total: {int(total)}")
print(int(total) < 158201495557678)
