"""
풀이 1. 문자열을 리스트(배열)로 변환
"""
def isPalindrome1(s: str) -> bool:
    str_as_list = []
    for char in s:
        # <str>.isalnum(): 스트링에 오직 숫자/문자만 있을 경우 True, 특수문자 또는 공백이 1개라도 있을 경우 False.
        if char.isalnum():
            str_as_list.append(char.lower())

    while len(str_as_list) > 1:
        # 리스트의 맨 앞에 있는 숫자를 pop()할 때 시간복잡도 = O(n) (뒤에 있는 값들을 앞으로 시프팅하기 때문에)
        # 리스트의 맨 뒤에 있는 숫자를 pop()할 때 시간복잡도 = O(1)
        if str_as_list.pop(0) != str_as_list.pop():
            return False
    return True

    # 문자열의 길이에 해당하는 횟수만큼 리스트의 맨 앞/뒤 숫자를 pop() 하므로 전체 시간복잡도 = O(n) * O(n) = O(n^2)


"""
풀이 2. 문자열을 덱(deque)으로 변환
"""
from collections import deque


def isPalindrome2(s: str) -> bool:
    str_as_deque = deque()

    for char in s:
        if char.isalnum():
            str_as_deque.append(char.lower())

    while len(str_as_deque) > 1:
        # 덱의 맨 앞에 잇는 숫자를 pop()할 때 시간복잡도 = O(1) (맨 앞 숫자를 가리키는 포인터만 이동시키면 되므로)
        # 덱의 맨 뒤에 있는 숫자를 pop()할 때 시간복잡도 = O(1) (맨 뒤 숫자를 가리키는 포인터 이동)
        if str_as_deque.popleft() != str_as_deque.pop():
            return False
    return True

    # 덱의 길이에 해당하는 횟수만큼 덱의 맨 앞/뒤 숫자를 pop() 하므로 전체 시간복잡도 = O(n) * O(1) = O(n)


"""
풀이 3. 문자열 슬라이싱(slicing)
"""
import re


def isPalindrome3(s: str) -> bool:
    # 정규표현식으로 특수문자, 공백을 ''으로 대체.
    refined_str = re.sub('[^a-z0-9]', '', s)
    
    # 슬라이싱으로 정제된 문자열을 뒤집어서 원래 문자열과 비교.
    return refined_str == refined_str[::-1]

    # 전체 시간복잡도 = O(슬라이싱 하려는 문자열 길이)
    # https://wiki.python.org/moin/TimeComplexity
