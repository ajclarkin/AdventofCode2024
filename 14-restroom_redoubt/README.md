# Restroom Redoubt

The first part of this was easy. The second part was actually easy too, although I thought it was going to be much harder.

### Features

Modular arithmetic, finding geometric patterns.


## Part 1
This was easy - find the position of all the robots 100 seconds from now. So, add on 100 x and y motions and use modular
arithmetic to ensure that the robots stay on the tiled area as they teleport from one side of the room to the other.

Finding the quadrants was just looking at the coordinates of each robot.


## Part 2

Initially I thought this was going to be a nightmare. Then I made an assumption that the tree would be in then middle and
the only filled in boxes and so thought I could look for a mirroring in the left and right. Before I started I happened to
see a picture of what it actually looks like on Reddit (while scrolling and not searching for this). New plan required. 
I thought it might be too touch but then thought: there's bound to be a few columns that run a significant length filled in.

So, what we do is repeatedly cycle, moving all the robots. Then record all the row coordinates for each column. Then look for
columns with more that 30 rows filled in. Thirty was trial and error, and I set a limit of 10,000 cycles to begin with. I added a 
pause for input after each one so that I could find the actual number of seconds, once I new my search had the tree in it. (For 
that I just ran it without the input and watched as everything flew by me.)
