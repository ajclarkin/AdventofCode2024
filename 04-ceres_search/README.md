# Ceres Search

Another nice one. Part two was quite different to part one in the approach. Direction finding always seems quite time-consuming to
write the code and I'm sure there must be an easier way. I know some folk use complex numbers but I've not got my head around that.

### Features
Direction finding, character finding and matching.


## Part 1

Read the map into a grid which is stored in a dictionary in the form `grid[(row, col)] = character`. At the same time keep a list of all the
positions of X. We'll also use a dict of possible moves that we can iterate through, and a function to add the movement to the current position.

Then, for each found X check the three positions in each possible movement direction to see if M, A, and S are found. I could have included a brek if
one of the earlier characters were not found but it ran fine without. Count all those positions which match.


## Part 2

At first glance it looks like regular expressions are the way to go but I soon realised it would be easier without.

Each cross begins at the top left with either M or S. All first lines begin either 'M S', 'S M', 'M M', or 'S S'. There's always an 
A on the next line one character over. So, scan through rows, looking for M or S. If one of these is found then check:
 - the character two to the right
 - the character one down and one over (A)
 - the character two down, and two down two over

If they all match then we've found a cross.
