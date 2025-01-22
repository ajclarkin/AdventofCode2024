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


    Values:
    [
        [
            C1,
            C2
        ]
    ]
```



## Part 2

The solution for part one should just work for part 2. But it didn't. Cue more learning about linear systems. Do I need to do something to reduce the target
like finding a common divisor? Nope - that doesn't make sense because there's still just one solution. I wondered if some of the equations were the same, for example `x + y = 3` and `2x + 2y = 6` but that would give an error 
and there are none.

So, my solution is correct but not working. Back to the text. The example doesn't have an answer to validate against, but it does state that only machines
two and four now work. Add some debugging print statements and it seems we're accepting the solution for *every* set, even though we shouldn't. So, or course, the 
problem is with `np.isclose()` - because one of the numbers we are comparing is 10,000,000,000,000 the relative tolerance component is far too large. It accepts
values +/- 10,000ish. So, I just had to change then relative tolerance to 1e-14.

Note that the tolerance applied is relative tolerance * abs(x) + absolute tolerance.


### References
[Maths is Fun - Linear Equations](https://www.mathsisfun.com/algebra/linear-equations.html)

[Maths is Fun - Solving Linear Equations using Matrices](https://www.mathsisfun.com/algebra/systems-linear-equations-matrices.html)

[LibreTexts Mathematics - 11. Systems of Equations and Inequalities](https://math.libretexts.org/Bookshelves/Algebra/Algebra_and_Trigonometry_1e_(OpenStax)/11%3A_Systems_of_Equations_and_Inequalities)
