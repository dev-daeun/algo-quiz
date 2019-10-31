from sys import stdin


def parent(i):
    return (i - 1) // 2


def left(i):
    return i * 2 + 1


def right(i):
    return i * 2 + 2


def sift_up(i):
    while i > 0 and tree[parent(i)] < tree[i]:
        tree[parent(i)], tree[i] = tree[i], tree[parent(i)]
        i = parent(i)


def sift_down(i):
    bigger = i
    while True:
        if left(i) < len(tree) and tree[left(i)] > tree[i]:
            bigger = left(i)
        if right(i) < len(tree) and tree[right(i)] > tree[bigger]:
            bigger = right(i)
        if bigger != i:
            tree[i], tree[bigger] = tree[bigger], tree[i]
            i = bigger
        else:
            return


def push(x):
    tree.append(x)
    i = len(tree) - 1
    sift_up(i)


def pop():
    if not tree:
        return 0

    if len(tree) == 1:
        root = tree.pop()
        return root

    root = tree[0]
    tree[0], tree[-1] = tree[-1], tree[0]
    tree.pop()
    sift_down(0)
    return root


N = int(stdin.readline())

tree = list()  # 0-index based
answer = []
for _ in range(N):
    num = int(stdin.readline())
    if num == 0:
        answer.append(pop())
    else:
        push(num)

for a in answer:
    print(a)
