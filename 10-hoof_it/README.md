# Hoof It

I came here having with part 2 of day 9 not giving the correct answer and I am *not* happy about it. (It works on all the examples, AoC and Reddit.) Anyway...

I liked this - unexpectedly simple. Find the paths going from 0 to 9 on a grid without diagonals. I used a DFS with a recursive algorithm and it worked nicely.
The second part was solved by the same code, just counting the recursive branches.


### Features
Recursion, depth first search, globals.


## Part 1

Build a grid in a dictionary with the key being the coordinates and the value being the character. At the same time save the position of the zeros and nines which we'll need later.
Now, for each nine follow each option avaiable until there are no more steps. If that's a zero then record in zeros that we got here from that particular nine.

At the end it's just a case of counting the unique nines reachable from each zero.

### Depth First Search

FindNeighbours() returns the points to N, E, S, W which are valid on the grid.

Zeros is a dictionary - the key is a tuple recording the grid position of the zero, and the value is a set recording which nines have are reachable from this zero.
Use a set to de-duplicate.

```python

def FollowPaths(point):
    neighbours = FindNeighbours(point) 
    neighbours = [x for x in neighbours if loc[point] - loc[x] == 1]
    if len(neighbours) == 0:
        if loc[point] == 0:
            global nine
            zeros[point].add(nine)
    else:
        for n in neighbours:
            FollowPaths(n)
```

## Part 2

The algorithm from part one solves this. Find how many paths exist between each zero and nine. So - that's counting the recursive branches which reach a zero.
