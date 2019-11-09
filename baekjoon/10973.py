from sys import stdin

N = int(stdin.readline())
perm = list(map(int, stdin.readline().split()))


def prev_permutation(perm):
    # 1. 순열의 맨 뒤에서부터 순회하면서 perm[i-1] > perm[i] 를 가장 먼저 만족하는 i를 찾는다.
    # 예)  i = 3, perm[i] = 1
    j = 0
    is_first = True
    for i in range(len(perm)-1, 0, -1):
        if perm[i-1] > perm[i]:
            j = i
            is_first = False
            break
    
    # 2. 위 조건을 만족하는 i가 없는 것은 순열이 오름차순, 즉 가장 첫번째 순열임을 뜻하므로 이전 순열이 없다고 리턴한다.
    if is_first:
        return None

    # 3. i <= x 이고 perm[i-1] > perm[x] 를 만족하는 x들 중에 최댓값을 찾는다.
    # 예) 7 2 4 1 3 5 6 에서 perm[i-1] = 4 일 때 max(1, 3) = 3
    num_to_swap = max(list(filter(lambda x: x < perm[j-1], perm[j:])))

    # 4. 위 조건을 만족하는 숫자를 perm[i-1]과 바꾼다.
    index_to_swap = perm.index(num_to_swap)
    perm[j-1], perm[index_to_swap] = perm[index_to_swap], perm[j-1]

    # 5. i ~ 마지막번째의 sub-list를 내림차순으로 정렬한다.
    return perm[:j] + sorted(perm[j:], reverse=True)


answer = prev_permutation(perm)
if not answer:
    print(-1)
else:
    print(' '.join([str(e) for e in answer]))


# test1
# input: 2
#        2 1
# output: 1 2

# test2
# input: 4
#        1 2 4 3
# output: 1 2 3 4

# test3
# input: 7
#        7 2 4 1 3 5 6
# output: 7 2 3 6 5 4 1
