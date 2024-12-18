# input = [int(x) for x in open('example.txt').read().split()]
input = [int(x) for x in open('input.txt').read().split()]

for i in range(25):
    new_input = list()
    for n in input:
        if n == 0:
            new_input.append(1)

        elif len(str(n)) % 2 == 0:
            n_len = len(str(n))
            n1 = int(str(n)[:n_len//2])
            n2 = int(str(n)[n_len//2:])
            
            new_input.append(n1)
            new_input.append(n2)

        else:
            new_input.append(n * 2024)

    input = new_input

print(f"Total length: {len(input)}")
