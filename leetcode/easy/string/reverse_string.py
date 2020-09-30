"""
풀이 1. two pointer 사용
"""
from typing import List


def reverseString1(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    len_of_s = len(s)
    for i in range(len_of_s // 2):
        start = i
        end = len_of_s - start - 1
        if start >= end:
            return
        s[start], s[end] = s[end], s[start]

    # 시간복잡도 = O(n)


"""
풀이 2. two pointer 사용 (1번 풀이보다 이해하기 더 쉬운 코드)
"""
def reverseString2(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    left = 0
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    # 시간복잡도 = O(n)


"""
풀이 3. 파이썬의 reverse() 사용.
"""
def reverseString3(s: List[str]) -> None:
    return s.reverse()


"""
풀이 4. 슬라이싱(slicing) 사용.
"""
def reverseString4(s: List[str]) -> None:
    s[:] = s[::-1]

    # https://www.notion.so/s-s-1-s-s-1-fbc236c83c404635a9c451c9c3720b03
