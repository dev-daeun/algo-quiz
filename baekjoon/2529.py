from itertools import permutations
from sys import stdin


K = int(stdin.readline().strip('\n'))
operators = stdin.readline().strip('\n').split()
MAX_NUM = 10


'''
시간복잡도: 
 브루트포스를 사용했을 경우 9! = 약 35만번의 연산을 하게되지만,
 조건을 만족하지 않으면 탐색을 멈추기 때문에 브루트포스 방법보다 훨씬 더 적은 연산을 한다.
'''


def is_satisfied(nums, num_idx1, num_idx2, op_idx):
    if operators[op_idx] == '>':
        # 조건을 만족하지 않으면 탐색을 멈춰야 한다.
        if not nums[num_idx1] > nums[num_idx2]:
            return False
        # 탐색을 멈추지 않고 맨 마지막 숫자까지의 검사를 마쳤다는 것은 주어진 부등식을 모두 만족한다는 것이므로 answers 대상에 들어간다.
        if num_idx2 == K:
            return True
    if operators[op_idx] == '<':
        if not nums[num_idx1] < nums[num_idx2]:
            return False
        if num_idx2 == K:
            return True

    # 숫자1 (부등호) 숫자2 => 숫자2 (부등호) 숫자3 => ... 순서로 부등식을 검사하기 위해 재귀를 사용한다.
    return is_satisfied(nums, num_idx2, num_idx2 + 1, op_idx + 1)


def get_answer():
    # 0 ~ 9 사이의 숫자를 각 1번씩만 사용하여 부등식을 만드므로(숫자들의 순서에 의미가 있다.) 순열을 사용하여 숫자리스트를 생성한다.
    perms = permutations(range(10), K + 1)
    answers = list()

    for nums in perms:
        result = is_satisfied(nums=nums, num_idx1=0, num_idx2=1, op_idx=0)
        if result:
            answers.append(int(''.join([str(n) for n in nums])))

    max_answer = str(max(answers))
    min_val = min(answers)

    if len(str(min_val)) < K + 1:
        min_answer = '0' + str(min_val)
    else:
        min_answer = str(min_val)

    print(max_answer)
    print(min_answer)


get_answer()
