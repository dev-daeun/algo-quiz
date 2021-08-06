def jumpingOnCloudsAnswer1(c):
    # Write your code here
    cur = 0
    answer = 0
    length = len(c)

    while True:
        if cur == length - 1:
            break
        if cur == length - 2:
            answer += 1
            break
        if c[cur + 2] == 0:
            cur += 2
        else:
            cur += 1
        answer += 1

    return answer


def jumpingOnCloudsAnswer2(c):
    cur = 0
    answer = 0
    length = len(c)

    while cur < length - 1:
        if cur + 2 < length and c[cur + 2] == 0:
            cur += 2
        else:
            cur += 1
        answer += 1

    return answer
