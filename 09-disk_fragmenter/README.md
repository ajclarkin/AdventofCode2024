# Disk Fragmenter 

Classic AoC. This is just crying out for an out-by-one error. Initially I wasn't sure I understood the instructions
but just read them and do as they say.

### Features

List insertions and deletions.

## Part 1 

I had various abortive starts, probably because there are a few ways I could have done this. After a trip to soft play
I came back and started anew with this.

Build a list of values representing each file space. The value of each element is the file ID. Since this increments only
with the real files and not the blanks we can use integer division when populating the list. I initially filled the spaces
with False but that had funny effects on the list, so I changed it to a character.

After the list was built I moved through it from start to end, replacing each space `type(char is not int)` with a value
popped off the end of the list. I checked that the popped value was an int and if not kept popping until I got one.

Both of these loops needed a slightly hand-crafted version because I was acting on a list that I was editing.

Finally just loop through and add up the ints, multiplying value by position.
