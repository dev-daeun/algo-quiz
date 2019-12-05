from itertools import combinations
from sys import stdin

L, C = list(map(int, stdin.readline().split()))
alphabets = stdin.readline().strip('\n').split()

jaum = list()
moum = list()


for alpha in alphabets:
    if alpha in 'aeiou':
        moum.append(alpha)
    else:
        jaum.append(alpha)

'''
num_of_j: 자음 리스트에서 조합을 선택할 때 최소로 선택하는 알파벳 수. (2 <= num_of_j <= L - 1)
num_of_m: 모음 리스트에서 조합을 선택할 때 최소로 선택하는 알파벳 수. (1 <= num_of_m <= L - 2)

num_of_j + num_of_m 이 L과 같을 때 두 수만큼 각각 자음/모음리스트에서 알파벳의 조합을 선택한다.
조합들을 순회하면서 비밀번호를 만든다.

시간복잡도: L * (L combination num_of_j) * (L combination num_of_m)
'''
answers = list()
for num_of_j in range(2, L):
    num_of_m = L - num_of_j
    if num_of_m >= 1:
            chosen_jaums = list(combinations(jaum, num_of_j))
            chosen_moums = list(combinations(moum, num_of_m))
            for j_com in chosen_jaums:
                for m_com in chosen_moums:
                    password = j_com + m_com
                    answers.append(sorted(password))


for ans in sorted(answers):
    print(''.join(ans))
