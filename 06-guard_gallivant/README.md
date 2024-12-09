# Print Queue

I liked this one - it was nice and easy. Straightforward direction following and using a cycle of directions to move through.

The second part takes a reasonable amount of time to run but not insane. So, I'm not sure at the moment if there's a better
algorithmic approach. I'll need to have a think or look on Reddit.

### Features
Direction following, cycle from itertools.

## Part 1

Easy. Parse the grid and get current position, then repeatedly move, checking to see if it's a space or an obstacle that we encounter.
If it's an obstacle then change direction by cycling through a list of directions, each one a right turn from the previous.

Count the unique coordinates we visit by using a set.


## Part 2

Do the same as above inside a loop. On each iteration we try converting one space into an obstacle and look to see if we visit the 
same coordinates while travelling in the same direction. If we do - it's a loop.
