from collections import defaultdict

# input = [int(x) for x in open('example.txt').read().split()]
input = [int(x) for x in open('input.txt').read().split()]

track = defaultdict(int)
for i in input:
    track[i] = 1



def Expand(n):
    if n == 0:
        return (1, False)

    elif len(str(n)) % 2 == 0:
        n_len = len(str(n))
        n1 = int(str(n)[:n_len//2])
        n2 = int(str(n)[n_len//2:])
        
        return (n1, n2)
    else:
        return (n * 2024, False)
    

for i in range(75):
    track_copy = track.copy()
    trackkeys = list(track_copy)

    for k, v in track_copy.items():
        if v > 0:
            track[k] -= v
        
            expansion = Expand(k)
            e1, e2 = expansion
            track[e1] += v

            if e2 is not False:
                track[e2] += v

length = sum(track.values())
print(f"{length}")
