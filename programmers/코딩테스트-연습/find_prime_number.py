from itertools import permutations

'''
문제 : https://programmers.co.kr/learn/courses/30/lessons/42839

N개의 중복가능한 숫자가 있을 때 1 ~ N개를 선택하여 소수인지 아닌지 판별하는 것.
1 ~ N개를 선택할 때 순서에 의미가 있으므로 permutations를 사용한다.
중복되는 수들로 만들어진 숫자는 무조건 1개로 취급한다.

중복되는 소수들을 unique하게 만들기 위해 마지막에 answers를 set()으로 형변환 했지만,
처음에 answers를 set()으로 정의하면 중복되는 숫자들에 의해 answers가 커지는 것을 방지할 수 있다.
'''
def is_prime(num):
    if num <= 1:
        return False

    for n in range(2, num // 2 + 1):
        if num % n == 0:
            return False
    return True


def solution(numbers):
    numbers = list(map(int, list(numbers)))

    answers = set()
    for i in range(1,  len(numbers) + 1):
        perms = permutations(numbers, i)
        for p in perms:
            num = int(''.join([str(n) for n in p]))
            if is_prime(num):
                answers.add(num)

    return len(answers)
