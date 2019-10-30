from math import factorial
from sys import stdin


# receive inputs
N = int(stdin.readline())
op, *inputs = list(map(lambda x: int(x), stdin.readline().split()))


def find_by_p(permutation):
    answer = 1
    numbers = [i for i in range(1, N+1)]
    for n in permutation:
        answer += (n - min(numbers)) * factorial(N - (permutation.index(n) + 1))
        numbers.remove(n)
    return answer


def find_by_k(k):
    pivot = sub = 1
    answer = list()
    numbers = [i for i in range(1, N+1)]
    perm_amount = factorial(N-sub)
    while True:
        if perm_amount < k:
            k -= perm_amount
            pivot += 1
        else:
            answer.append(pivot)
            numbers.remove(pivot)
            if not numbers:
                return answer
            numbers = sorted(numbers)
            pivot = numbers[0]
            sub += 1
            perm_amount = factorial(N-sub)


if op == 1:
    p = find_by_k(inputs[0])
    print(' '.join([str(n) for n in p]))
else:
    print(find_by_p(tuple(inputs)))
