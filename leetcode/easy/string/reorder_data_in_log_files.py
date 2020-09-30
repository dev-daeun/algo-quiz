from typing import List


"""
풀이 1. lambda 사용
"""
def reorderLogFiles1(logs: List[str]) -> List[str]:
    char_logs = []
    num_logs = []

    for log in logs:
        splited = log.split()
        try:
            int(splited[1])
        except ValueError:
            char_logs.append(log)
        else:
            num_logs.append(log)

    # 식별자를 제외한 문자열이 정렬의 우선순위가 되어야 하고
    # 문자열이 동일할 경우 식별자가 정렬의 우선순위가 되어야 한다. -> 람다 표현식이 (문자열, 식별자)가 되도록 한다.
    char_logs = sorted(char_logs, key=lambda x: (x.split()[1:], x.split()[0]))

    return char_logs + num_logs


"""
풀이 2. lambda, <str>.isdigit() 사용
"""
def reorderLogFiles1(logs: List[str]) -> List[str]:
    char_logs = []
    num_logs = []

    for log in logs:
        splited = log.split()
        if splited[1].isdigit():
            num_logs.append(log)
        else:
            char_logs.append(log)

    char_logs = sorted(char_logs, key=lambda x: (x.split()[1:], x.split()[0]))

    return char_logs + num_logs
