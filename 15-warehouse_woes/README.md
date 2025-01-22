# Warehouse Woes
THis was quite good. Part one was straightforward and then the second had a step up in difficulty which kept me busy. I felt like I was close to solving
it for a while.

### Features
Recursion


## Part 1
This was nice. I wrote a recursive function to check the possible movements: if the @ can move then move it but if there's a box in the way then
run the same algorithm on the box. It worked!


## Part 2
I made this look difficult. There were a few traps to avoid. I updated the part 1 algorithm but kept tripping up. Fortunately there were loads
of edge cases on Reddit to help me troubleshoot.

I use a recursive algorithm as before to see if I can move, but rather than doing the move at the time, I save a list of all the moves to be implemented.
Then, once I've confired that every recursion level can happen, I execute all of the saved moves. This allows for diverging branches where one branch might return true
and the others not.

I also had to make sure that I backfilled with empty correctly. So, if moving away from a wall, I shouldn't back fill the wall square with empty.
