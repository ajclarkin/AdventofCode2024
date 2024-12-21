# Plutonian Pebbles

This is one of those puzzles where the first part is easy (find n of something) and then the second part cannot be answered
with the same algorithm (find a much bigger n of something). The solution in part 1 is useful because it shows we have the 
logic correct - in this case that's transforming the pebblems.

Part 2 caused some difficulty but in the end I liked it.

### Features
Defaultdict, replacing one number with another, keeping track of how many of each.


### Data Structure

The input is a series of numbers and we're going to transform those repeatedly, according to some rules.
In part 1 I just stored them in a list and then replaced each one with the transformed values. (Well, I also
used a copy so that I didn't edit a list I was working through.)

In part 2 I used a defaultdict from Collections. This solved the problem of wanting to add increment the values of an 
item where that item didn't exist yet in the dictionary. Defaultdict solves this by having a default type when the key doesn't exist.

```python
track = defaultdict(int)

track[12] += 1
# we haven't added [12] to track yet so it will default to an int of value 0

```

## Part 1
Read the input into a list and create a new blank list. Iterate through the former, making the changes, and inserting those changes into
the new list. Copy the new list to the old then repeat again, looping as many times as needed.


## Part 2
You can't use part 1 - it expands too much and so once into the 30s for loops it slows down. I had a few ideas but (a little) help from Reddit saw me right.
This time we use a defaultdict with the key equal to the value of the pebble and the value storing the number of those pebbles. On each loop we work through the keys,
replacing them in the dict with what they get expanded to.

Note that I had to use a copy to make sure that I didn't decrement the count of various keys after they had been increased on this round. I also tried
setting the count of a key to zero when expanding it but that broke things because you might already have increased this count on this round with an expansion.
Instead I decremented the count by the number of present at the end of the last round, and that needed the copy taken at the end of the last round.

### Further Reading
The following tutorial covers recursion and memoisation.
(Reddit Tutorial)[https://www.reddit.com/r/adventofcode/comments/1hbnyx1/2024_day_11python_mega_tutorial/]
