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


def get_results(meetings, n):
    results = [0 for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(i+1):
            if j + meetings[j].term - 1 <= i:
                results[i] = max(results[i], results[j-1] + meetings[j].pay)
    return results[-1]

inputs = create_inputs(N)
print(get_results(inputs, N))