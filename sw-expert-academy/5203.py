import itertools

n = int(input())

answers = []


def is_run(it):
    a, b, c = it
    return c == b + 1 and b == a + 1


def is_triplet(it):
    a, b, c = it
    return a == b and b == c


def baby_gin(cards):
    p1 = []
    p2 = []
    for i, c in enumerate(cards):
        if i % 2 == 0:
            p1.append(c)
        else:
            p2.append(c)

        if (len(p1) >= 3 and len(p2) >= 3) and (len(p1) == len(p2)):
            p1_permutate = itertools.permutations(p1, 3)
            is_p1_baby_gin = False
            for p in p1_permutate:
                if is_run(p) or is_triplet(p):
                    is_p1_baby_gin = True
                    break

            p2_permutate = itertools.permutations(p2, 3)
            is_p2_baby_gin = False
            for p in p2_permutate:
                if is_run(p) or is_triplet(p):
                    is_p2_baby_gin = True
                    break

            if is_p1_baby_gin and not is_p2_baby_gin:
                return 1

            if is_p2_baby_gin and not is_p1_baby_gin:
                return 2

    return 0


for _ in range(n):
    cards = list(map(lambda x: int(x), input().split()))
    answers.append(baby_gin(cards))


for ans in answers:
    print('#{} {}'.format(answers.index(ans) + 1, ans))
