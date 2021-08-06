from collections import Counter


def sockMerchantAnswer1(n, ar):
    c = Counter(ar)
    answer = 0
    for _, socks_per_color in c.items():
        answer += socks_per_color // 2
    return answer


def sockMerchantAnswer2(n, ar):
    table = {}
    answer = 0
    for sock in ar:
        if not table.get(sock):
            table[sock] = 1
        else:
            table[sock] += 1
            if table[sock] % 2 == 0:
                answer += 1
                table[sock] = 0
    return answer
