from sys import stdin
import pprint


N, M = list(map(int, stdin.readline().split()))
P = list()
for _ in range(N):
    row = list(stdin.readline().strip('\n'))
    P.append(row)


def calculate_width_sum(width_set):
    width_pieces = [list() for _ in range(N)]

    for n in range(N*M):
        if n & width_set:
            share = n // M
            rest = n % M
            width_pieces[share].append(P[share][rest])

    pp = pprint.PrettyPrinter(indent=2)
    
    pieces = list()
    for nums in width_pieces:
        if nums:
            pieces.append(int(''.join(nums)))

    pp.pprint(f'width: {pieces}')

    return sum(pieces)


def calculate_height_sum(height_set):
    height_pieces = [list() for _ in range(M)]

    for n in range(N*M):
        if n & height_set:
            share = n // M
            rest = n % M
            height_pieces[rest].append(P[share][rest])
    
    total_sum = 0
    for li in height_pieces:
        total_sum += sum(list(map(int, li)))
    
    if total_sum == 0:
        return 0
    
    pp = pprint.PrettyPrinter(indent=2)

    pieces = list()
    for nums in height_pieces:
        if nums:
            pieces.append(int(''.join(nums)))

    pp.pprint(f'height: {pieces}')
    return sum(pieces)


def get_answer():
    U = (1 << (N * M)) - 1
    answer = 0
    for width_set in range(1 << (N * M)):
        height_set = U - width_set
        
        print('--------------------')
        width_sum = calculate_width_sum(width_set)
        height_sum = calculate_height_sum(height_set)
        answer = max(answer, width_sum + height_sum)
    return answer

print(get_answer())
