# Mull It Over

I think I'm growing to love regexes, probably after needing them so often last year.

This was quite a nice little challenge and felt like appropriate difficulty for day 3. I'm still on track but there's
some on-call coming up.


### Regex Use

Here I used re.search() which returns a match group: `<re.Match object; span=(20, 27), match="don't()"`
Thie span can be accessed using `m.span()` and accessing the tuple as usual. The match is a string accessed
using m.group(0) - all assuming that the return value of re.search is assigned to m.

## Part 1

Nice and easy - find the patterns that match and multiple the two numbers. I used a regex to find them and remembered from
last year to put the digits in () which created capture groups for me to use.

(Regular Expressions 101)[https://regex101.com/] was again a helpful website.


## Part 2

Now we need to only include the multiples identified if they are preceeded by do() and exclude them if preceeded by don't().
No we'll use regex to find the positions of these first.



For each line in the input we're going to start in include mode - including matches - 
until we get to a don't, then set the include to false. That will toggle as we go along.
We read in each line as a string, find the position of the next do / don't, and then if in
include mode we'll multiple them and add to total. Thereafter trim off that part of string that we've
checked and repeat.
