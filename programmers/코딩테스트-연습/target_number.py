'''
문제 : https://programmers.co.kr/learn/courses/30/lessons/43165

numbers[i] 다음으로 가능한 것 : -numbers[i], +numbers[i]
numbers를 모두 순회하면서 sum한 결과가 target과 같으면 answer += 1 한 후에 함수를 종료한다.
'''

def solution(numbers, target):
    get_answer(numbers, 0, 0, target)
    return answer


answer = 0


def get_answer(numbers, sum_, idx, target):
    global answer
    if idx == len(numbers):
        if sum_ == target:
            answer += 1
    else:
        get_answer(numbers, sum_ + numbers[idx], idx + 1, target)
        get_answer(numbers, sum_ - numbers[idx], idx + 1, target)
