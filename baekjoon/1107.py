from sys import stdin

MAX_ = 500000
CURRENT = 100

dest = int(stdin.readline())
N = int(stdin.readline())
broken_buttons = list(map(lambda x: int(x), stdin.readline().split()))


def get_answer():
    dest_list = [int(e) for e in str(dest)]
    channel_to_jump = list()
    answer = abs(dest - CURRENT)

    able_buttons = list()
    for b in range(10):
        if b not in broken_buttons:
            able_buttons.append(b)

    if not able_buttons:
        return answer

    for i in range(len(dest_list)):
        min_ = min([abs(dest_list[i] - b) for b in able_buttons])
        channel_to_jump.append(abs(dest_list[i] - min_))

    if channel_to_jump == [0 for _ in range(len(channel_to_jump))]:
        return answer

    channel_to_jump = int(''.join(str(n) for n in channel_to_jump))
    answer = min(answer, abs(dest - channel_to_jump) + len(dest_list))

    return answer


print(get_answer())


# test1
# input:
# 5457
# 3
# 6 7 8
# output:
# 6

# test2
# input:
# 500000
# 8
# 0 2 3 4 6 7 8 9
# output:
# 1117

# test3
# input:
# 100
# 1
# 1
# output:
# 0

# test4
# input:
# 500000
# 10
# 0 1 2 3 4 5 6 7 8 9
# output:
# 499900

# test5
# input:
# 200
# 9
# 1 2 3 4 5 6 7 8 9
# 100

# test6
# input:
# 100000
# 9
# 0 1 2 3 4 5 6 7 8
# output:
# 6
