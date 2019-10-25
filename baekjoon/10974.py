import itertools

n = int(input())

li = range(1, n+1)

p = itertools.permutations(li)

for pair in p:
    for element in pair:
        print(element, end=' ')
    print()

