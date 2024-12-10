# Bridge Repair

Ok, 2024 is going well. I thought this was going to be the first one that was a complete
nightmare, but I was wrong. I initialy came up with a solution that should have worked and
then discarded it assuming that the data would make it perform too slowly. Wrong.

I did the same for part 2 too. Sometimes you just need to test the straightforward and see 
if it fails before trying the complicated.

### Data Structure

The structure is a value we want to make and then a series of ints to make it from. I couldn't
use a dictionary because it was possible that more than one row would have the same target value
(I didn't check). So, I used a tuple of target value and list of ints.

```
Input:
7290: 6 8 6 15

After Processing:
[(7290, [6, 8, 6, 15]), ]
```


### Features

Combinatorics using itertools.product, regex, integer concatentation, altering a list while
iterating.


## Part 1
I started off by making this far too complicated, based on my history with AoC. I thought about
making this more efficient by storing the value of each pair of additions and multiplications
for later lookup. I also thought I might be able to write a recursive algorithm - but I did not.

So, first parse the input, making sure to remove blanks of course. Then create a list of the
operations which could go in there. For n integers in the list there are n-1 operations, and for
each operation there are two options: add and multiply. I used `product()` to create the 
combinations of operations and then just cycled through the list, applying the operation.

I included a break statement so once the value was found or could not be found because the
running total was to high, the evaluation moved on.


## Part 2

This time we add a third operation: concatentation. I messed around with a couple of options
but it was actually super simple.

 - First run the algorithm as before and remove the equations which evaluate to true - the part 1
 solution.
 - For the equations that remain run the process again but this time include concatentation in the
 available list of operations.

Don't remove an item from a list while iterating through it - it's not worth it. I used a copy to 
track the changes instead. I converted the application of the operations to a function so that 
it could be run twice to allow for the first and second search.

```
# String concatenation
# To join 12 and 36:
int(str(12) +str(36))
```
