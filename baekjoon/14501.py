from sys import stdin

N = int(input())


class Meeting:
    def __init__(self, term, pay):
        self.term = term
        self.pay = pay


def create_inputs(n):
    inputs = [Meeting(term=0, pay=0)]
    for _ in range(n):
        t, p = list(map(lambda x: int(x), stdin.readline().split()))
        inputs.append(Meeting(term=t, pay=p))
    return inputs


"""
result[i]    = i일에 얻을 수 있는 최대 총 금액

금액을 받는 날 = 일이 끝나는 날   ex) 2일에 이틀걸리는 일을 시작함 ===> 3일에 금액 받음

  j일에 일을 시작했다면 일이 끝나는 날인 (j + T[j] - 1)일에 가질 수 있는 총 금액
= (j-1)일에 받았던 총 금액 + p[j]
= results[j-1] + p[j]
""" 
def get_results(meetings, n):
    results = [0 for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(i+1):
            if j + meetings[j].term - 1 <= i:
                results[i] = max(results[i], results[j-1] + meetings[j].pay)
    return results[-1]

inputs = create_inputs(N)
print(get_results(inputs, N))