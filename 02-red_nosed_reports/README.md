## Red-Nosed Reindeer

Another nice one, pretty straight-forward although it took me long enough. Ten minutes away from the computer clarified it all for me though.Another


### Part 1

Read the file line by line (splitting at newline). Then turn each line into a list of multiple integers.

The basic algorithm here is:
 - Loop through all the rows in the input.
 - For each line, compare it to a sorted version of itself (forwards and reverse) to assess whether sorted correctly.
 - If sorted correctly:
   - Compare each pair of sequential characters for an approriate difference (1 to 3) in ascending or descending order.
   - Keep assessing until all characters checked and in appropriate order, then return 1.
   - If a pair doesn't have appropriate difference then fail - break out of loop and return 0.


The we just need to count the number of rows which returned 1.


### Part 2

Same task but this time we need to see if failing lines could be made to pass by removing one number.

My code was initially a bit untidy but it came together. We use the same algorithm above but this time when 
we loop through the list of lines we then create a new list with the individual line we want to consider and the 
other variants created by deleting each consituent element in turn. From there we loop through the new list and
test for correct sort order and differences as before.
