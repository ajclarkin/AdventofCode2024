# Historian Hysteria

This was a nice easy entry, exactly what day 1 should be.

The input is two numbers per line, separated by a space. Read it in using a listcomp then split into left and right by slicing.


### Features

These use zip, counter, and list slicing.

## Part 1

Sort both lists (left and right) then find the absolute difference between each in a pairwise manner. Sum the differences.

I used `zip()` to work through the two lists but equally I could have just iterated through them.


## Part 2

This time don't sort. Multiple each element in the left list by the count of that element in the right list and sum these values.
I used a `Counter()` which made it simple.
