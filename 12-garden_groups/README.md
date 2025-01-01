# Garden Groups 

Part one was ok once I got my head around it, part two was a nightmare. However, when I got a pad and pen out and started
to think about it some patterns became clear. Eventually I got there.

It's a rectilinear grid area and perimeter problem.

### Features

Flood fill. Identifying perimeters and corners of rectilinear structures.


## Part 1

Read the grid into a dict as usual, with a tuple of (row, col) as the key and the crop letter as the value.

Do a flood fill, which is pretty much the same as a breadth first search (or at least, I thought I was doing a 
BFS at the time) and record each cell in the current crop in a dict where the key is the first cell of that crop.

When identifying neighbours to populate the queue I also counted how many there were in the current area. If 
fewer than four then that meant the cell was a perimeter cell, and so I added that to a running total of the perimeter
cells.
 

## Part 2

This took a lot of work.

Things to note:
 - The number of sides is the same as the number of corners.
 - A rectilinear shape can have convex and concave corners. (Probably not the right term.)
 - Total number of corners is equal to 4 + (convex - 4) * 2.

So I had to work out how to define a corner. Consider a 2x2 block - which is always what constitutes a corner. The
cell in question could form a corner on any of the four diagonals, so they all need to be checked.

*Convex Corner*
 - The diagonal can be of the same crop or different.
 - The two other blocks (henceforth called shoulder blocks) are not of the same crop.

```
A convex corner in A - the diagonal and shoulders are crop B:

  BB
  BA
```

*Concave Corner*
- The diagonal must be a different crop.
- The two shoulder blocks are the same crop.

```
Convave corners in A - the diagonal and shoulders are crop B.
The second example shows a tricky case where there are two areas of crop B and
two concave corners.

           AAAA
  BA       ABAA
  AA       AABA
           AAAA
```

So, the solution was to calculate the areas as before and this time save the locations of the perimeters
instead of the count. I had to make sure and count cells where only the diagonal neighbours were different crops
as perimeters too, to account for the second example in the block above.

After building a list of perimeters per area, loop through them and for each of the four diagonal directions,
 heck to see if the corner criteria described above were met. Keep a track of the number of corners found.

Then the final answer could be calculated in the same way as before.

