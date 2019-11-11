from sys import stdin

N, S = list(map(int, stdin.readline().split()))
arr = list(map(int, stdin.readline().split()))


# i : pow(2, N)개의 각 집합.
# k : arr안의 각 숫자들의 비트마스크.
# 예)
# i = 1 0 1 0 1
# k = 0 0 1 0 0
# i & k => k번째 숫자가 집합 i 안에 들었을 경우(AND 연산으로 파악) 더하기. -> i번째 집합에 있는 숫자들의 sum이 S와 같을 경우 cnt 증가. 
def get_answer():
    cnt = 0

    for i in range(1, 1 << N):  # 1 << N 은 pow(2, N)과 동일.
        sum_ = 0
        for k in range(N):
            if i & (1 << k):
                sum_ += arr[k]
        
        if sum_ == S:
            cnt +=1

    return cnt


print(get_answer())
