input = [x for x in open('input.txt').read().split('\n') if len(x) > 0]
# input = [x for x in open('example.txt').read().split('\n') if len(x) > 0]

# Split the input into the page ordering rules and the pages to be ordered
rules = [x for x in input if '|' in x]
pages = [x for x in input if '|' not in x]


# For each digit with a rule, make an entry in the correct dictionary, using the digit as the key
# and a set containing all the digits as the values.
preceeded_by = dict()
followed_by = dict()

for r in rules:
    before, after = map(int, r.split('|'))

    if before not in followed_by:
        followed_by[before] = set()
    
    followed_by[before].add(after)


    if after not in preceeded_by:
        preceeded_by[after] = set()
    preceeded_by[after].add(before)



    
# Now we have a dict for each of the rules
# We need to use these dicts using sets.issubset() to work out if the pages are in the right order.
# a.issubset(b) will test to see if all the values of a are in b and return True or False, depending on the values.
valid_lists = list()

for page in pages:
    # Up until now the stored version is a string containaing all the values. Parse into list of ints.
    current = [int(x) for x in page.split(',')]

    for n, char in enumerate(current):
        front = set(current[:n])
        back = set(current[n+1:])

        # if n ==  0 then there's nothing in front to check
        # other wise check everything in front is in preceeded_by
        if n == 0:
            pass
        elif char in preceeded_by and not front.issubset(preceeded_by[char]):
            break

        if n == len(current)-1:
            pass
        elif char in followed_by.keys() and not back.issubset(followed_by[char]):
            break
    else:
        # get here if the criteria are all met
        valid_lists.append(current)
            

total = 0
for vl in valid_lists:
    total += vl[len(vl) // 2]
print(f"Final total is {total}")
