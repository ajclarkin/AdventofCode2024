# Resonant Collinearity

Nice and easy today. The description for part 2 was a bit confusing but I think that was deliberate.


### Features

Coordinates, combinations, greatest common divisor.


## Part 1 

Scan the grid and save the position of the antennae. Use combinations from itertools to find unique pairs and calculate
the x and y distance between them. Now repeatedly subtract that distance from the first one and add it to the second one,
terminating that loop when out of grid bounds. Add the newly found points to a set.


## Part 2

Every point on the line created by the antennae pair can now be an antinode. So, again find the distance but then divide
by the greatest common divisor in case there's a pair of antennae which are something like 4,2 apart. Then repeatedly add 
or subtract multiples of this to the original points. Note that to allow for points between the two antennae we add to the first
point and subtract from the second; the overlap will be prevented by using a set. Note that it looks like we didn't need the gcd() trick.

It took a bit of time to get this right - initially I did it the same way as part one so missed out the points inbetween.
