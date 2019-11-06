from sys import stdin

E, S, M = list(map(lambda x: int(x), stdin.readline().split()))

E_MAX = 15
M_MAX = 19
S_MAX = 28
MAX_ = E_MAX * S_MAX * M_MAX


# i % *_MAX = 0 일 경우
# (ex. 입력값이 11 28 18 이고 출력해야 하는 값이 56인 경우 i % S_MAX = 0 는 참이고 S = 28 이어야 함.)
# 어떻게 처리해야 할 지 몰라서 시간 다소 소요. 
# S == S_MAX 조건문 추가로 해결.
def get_answer_1():
    if E == S == M:
        return E
    for i in range(1, MAX_ + 1):
       if (((i % E_MAX == E) or (i % E_MAX == 0 and E == E_MAX)) and
           ((i % M_MAX == M) or (i % M_MAX == 0 and M == M_MAX)) and 
           ((i % S_MAX == S) or (i % S_MAX == 0 and S == S_MAX))):
           return i


# 코드플러스 답
def get_answer_2():
    if E == S == M:
        return E

    e = s = m = answer = 1
    while True:
        if e == E and s == S and m == M:
            return answer
        e += 1
        s += 1
        m += 1
        if e == E_MAX + 1:
            e = 1
        if s == S_MAX + 1:
            s = 1
        if m == M_MAX + 1:
            m = 1
        answer += 1

print(get_answer_1())
print(get_answer_2())

# test1
# input: 1 1 1
# output: 1
#
# test2
# input: 1 16 16
# output: 16
# 
# test3
# input: 15 15 15
# output: 15
#
# test4
# input: 13 28 9
# output: 28
# 
# test5
# input: 14 1 10
# output: 29 
#
# test6
# input: 4 19 19
# output: 19
#
# test7
# input: 5 20 1
# output: 20