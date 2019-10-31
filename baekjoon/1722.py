from math import factorial
from sys import stdin


def test1():
    n = 4
    k = 3
    answer = find_by_k(n, k)
    print('test 1: ', answer)
    assert answer == [1, 3, 2, 4]


def test2():
    n = 4
    p = (1, 3, 2, 4)
    answer = find_by_p(n, p)
    print('test 2: ', answer)
    assert answer == 3


def test3():
    n = 5
    k = 118
    answer = find_by_k(n, k)
    print('test 3: ', answer)
    assert answer == [5, 4, 2, 3, 1]


def test4():
    n = 20
    k = 2432902008176640000
    answer = find_by_k(n, k)
    print('test 4: ', answer)
    assert answer == [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


def find_by_p(n, permutation):
    answer = 1
    numbers = [i for i in range(1, n+1)]
    for num in permutation:
        answer += (num - min(numbers)) * factorial(n - (permutation.index(num) + 1))
        numbers.remove(num)
    return answer


def find_by_k(n, k):
    pivot = sub = 1
    answer = list()
    numbers = [i for i in range(1, n+1)]
    perm_amount = factorial(n-sub)
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
            perm_amount = factorial(n-sub)


test1()
test2()
test3()
test4()

# # receive inputs
# N = int(stdin.readline())
# op, *inputs = list(map(lambda x: int(x), stdin.readline().split()))
#
# if op == 1:
#     p = find_by_k(inputs[0])
#     print(' '.join([str(n) for n in p]))
# else:
#     print(find_by_p(tuple(inputs)))

