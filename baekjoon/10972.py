from sys import stdin

N = int(stdin.readline())
perm = list(map(int, stdin.readline().split()))


def next_permutation(perm):
    j = 1
    is_last = True
    for i in range(len(perm)-1, 0, -1):
        if perm[i-1] < perm[i]:
            j = i
            is_last = False
            break
    
    if is_last:
        return None

    sub_value = perm[j-1]
    index_to_swap = j - 1
    for k in range(j, len(perm)):
        if perm[j-1] < perm[k] and perm[k] - perm[j-1] < sub_value:
            index_to_swap = k
            sub_value = perm[k] - perm[j-1]

    perm[j-1], perm[index_to_swap] = perm[index_to_swap], perm[j-1]

    return perm[:j] + sorted(perm[j:])


answer = next_permutation(perm)
if not answer:
    print(-1)
else:
    print(' '.join([str(e) for e in answer]))