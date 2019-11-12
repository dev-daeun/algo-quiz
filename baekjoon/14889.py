from sys import maxsize, stdin

N = int(stdin.readline())

P = list()
for _ in range(N):
    P.append(list(map(int, stdin.readline().split())))


def add_power(s, n):    
    power = 0
    for i in range(N):
        if s & (1 << i):
            power += P[i][n]
            power += P[n][i]
    
    return power


def get_answer():
    U = (1 << N) - 1
    answer = maxsize

    for s1 in range(1 << N):
        s2 = U - s1
        
        s1_cnt = 0
        s2_cnt = 0
        
        s1_power = 0
        s2_power = 0

        for n in range(N):
            if s1 & (1 << n):
                s1_cnt += 1
                s1_power += add_power(s1, n)
            else:
                s2_cnt += 1
                s2_power += add_power(s2, n)

        if s1_cnt == s2_cnt == (N / 2):
            answer = min(answer, abs(s1_power - s2_power))
    
    return answer


print(get_answer())
