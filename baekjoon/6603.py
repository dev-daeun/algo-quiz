import itertools
import sys

answers = []
while True:
    input_ = input()
    if input_ == '0':
        for ans in answers:
            for line in ans:
                for num in line:
                    print(num, end=' ')
                print()
            print()
        sys.exit()

    k, *S = list(map(lambda x: int(x), input_.split()))
    answers.append(list(itertools.combinations(S, 6)))

