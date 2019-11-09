from sys import stdin

N = int(stdin.readline())
perm = list(map(int, stdin.readline().split()))


def next_permutation(perm):
    # 1. 순열의 맨 뒤에서부터 앞으로 순회하면서 perm[i-1] < perm[i] 를 가장 먼저 만족하는 i를 찾는다.
    # 예) 7 2 3 6 5 4 1 에서 위 조건을 만족하는 i = 3, perm[i] = 6 
    j = 1
    is_last = True
    for i in range(len(perm)-1, 0, -1):
        if perm[i-1] < perm[i]:
            j = i
            is_last = False
            break
    # 2. 위 조건을 만족하는 i가 없는 것은 전체 순열이 내림차순, 즉 가장 마지막 순열임을 뜻하므로 다음 순열은 없다고 리턴한다.
    if is_last:
        return None
    
    # 3. i-1 <= x 이고 perm[i-1] < perm[x] 를 만족하는 것들 중에서 최소값을 찾는다. 
    # 예) 7 2 3 6 5 4 1 에서 perm[i-1] = 3 일 때 위 조건을 만족하는 최소값 = min(6, 5, 4, 1) = 4
    num_to_swap = min(list(filter(lambda x: x > perm[j-1], perm[j:])))

    # 4. perm[i-1] 과 위 조건을 만족한 perm[x] 의 값을 swap한다.
    index_to_swap = perm.index(num_to_swap)
    perm[j-1], perm[index_to_swap] = perm[index_to_swap], perm[j-1]

    # 5. i ~ 마지막 번째 sub-list 를 오름차순으로 정렬한다.
    return perm[:j] + sorted(perm[j:])


answer = next_permutation(perm)
if not answer:
    print(-1)
else:
    print(' '.join([str(e) for e in answer]))


# test1
# input: 2
#        1 2
# output: 2 1

# test2
# input: 4
#        1 2 3 4
# output: 1 2 4 3

# test3
# input: 7
#        7 2 3 6 5 4 1
# output: 7 2 4 1 3 5 6