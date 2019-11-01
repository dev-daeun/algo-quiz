from sys import stdin

ages = []
names = []


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def is_leaf(i):
    return i >= N // 2


# min-heap by age.
# if ages are same, node with smaller index should be a parent.
def sift_down(i):
    smaller = i
    is_right_smaller = False

    while not is_leaf(i):
        if left(i) < N and ages[i] > ages[left(i)]:
            smaller = left(i)

        if right(i) < N and ages[smaller] > ages[right(i)]:
            smaller = right(i)
            is_right_smaller = True

        if smaller != i:
            ages[i], ages[smaller] = ages[smaller], ages[i]
            names[i], names[smaller] = names[smaller], names[i]

            if is_right_smaller and ages[smaller] == ages[left(i)]:
                names[smaller], names[left(i)] = names[left(i)], names[smaller]

        i = smaller


def build_heap():
    for i in range(N // 2):
        sift_down(i)


N = int(stdin.readline())
for _ in range(N):
    age, name = stdin.readline().split()
    ages.append(int(age))
    names.append(name)

build_heap()

for age, name in zip(ages, names):
    print('{} {}'.format(age, name))
