# Print Queue

This one took a bit longer but that was mostly because I had a presentation to write and deliver at work. I
really need to try and get back on track. It was a nice one and appropriate level for day 5 and I enjoyed it.


### Features
Sets, bubblesort.


## Part 1
Parsing the input looked like it might be a faff but was actually simple, matching on whether or not the line had | in it.
I should have converted the second part of the input to ints before starting but didn't, and so kept it the same for part 2.

So, make a list of rules and pages. Split the rules into separate ints and then insert into dictionaries preceeded_by[] and followed_by[]
so for each number I could see what needed to come before it and after it. The values in the dicts were sets to keep everything 
unique.

Then, for each set of pages for printing, go through them, looking to see if the rules are adhered to.

> [1, 2, 3, 4]
> 
> 1: nothing to check in preceeded_by, check {2, 3, 4} in followed_by[1]
> 
> 2: check preceeded_by[2] for {1} and followed_by[2] for {3, 4}
> 
> 3: check preceeded_by[3] for {1, 2} and followed_by[3] for {4}
> 
> 4: check preceeded_by[4] for {1, 2, 3} and nothing to check in followed_by.


Once we've found the lists that are correctly ordered, find the middle element.
`value = list[len(list) // 2]`
The integer division gives the answer we need.


## Part 2
First adjust the code from part one to identify the lists which are not correctly ordered.
Then sort each one using bubblesort - cycle through each one, checking it against the rules (rather than ascending numbers)
and swapping if required.
 
I did try using quicksort for this but with the rules in place and the need to check if there was an entry in the lookup dict for
each value, bubblesort was much simpler.
