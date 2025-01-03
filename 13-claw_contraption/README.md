# Claw Contraption

Ok, simultaneous equations, I think. Every so often in my life this crops up and I get annoyed 
because I can't remember how to solve them, and then I look it up. I also vaguely remember using matrices
to solve more complex problems and have been meaning to study that.

Given a series of claw machines with two buttons, A and B, you have to position the claw exactly at an x,y coordinate.
Each button moves the claw a different amount of x and y. A costs more than B. Find the cost of the claws which can
actually be moved to the target location.


### Features

Linear algebra, systems of equations, simultaneous equations.


### Data Structure

The input comes as three lines per machine.
```
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400



```

I read each triple of lines into a list then read the values using regular expressions.

```python

input = [x for x in open('input.txt').read(). split('\n\n') if len(x) > 0]

for i in input:
    nums = [int(x) for x in re.findall("\d+", i)]
    coefs = np.array([[nums[0], nums[2]], [nums[1], nums[3]]])
    values = np.array(nums[4:])
```

The values are then entered into a structure compatible with matrix operations.

```
    Coefficients:
    [
        [
            [A1, A2],
            [B1, B2]
        ],
    ]
```
