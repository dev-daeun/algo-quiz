"""
어떤 배열이 valid mountain 이고 i번째에서 봉우리가 있다고 할 때,

1. 0 부터 i 까지 ascending 이 1번 선행되어야 하고
2. i 부터 len(A)-1 까지 descending 이 1번 후행되어야 함.

V자 형태로 descending이 ascending보다 먼저 나타나거나
\ 또는 / 형태와 같이 descending만 있거나 ascending만 있을 경우 valid mountain이 아니다.


 - 솔루션 -
ascend : 배열 안에서 내림차순 형태가 나타났는지 여부를 체크하는 용도.
descend : 배열 안에서 오름차순 형태가 나타났는지 여부를 체크하는 용도.

인접하는 두 숫자가 ascend 할 경우 descend 가 먼저 선행되었다면 유효하지 않으므로 False를 리턴.
인접하는 두 숫자가 descend 할 경우 ascend 가 먼저 선행되지 않았다면 유효하지 않으므로 False를 리턴.
인접하는 두 숫자의 크기가 같으면 유효하지 않으므로 False를 리턴.

ascend 와 descend 가 둘 다 나타났는지 여부는 ascend & descend 의 결과로 알 수 있다.

시간복잡도 : 배열을 선형으로 순회하므로 O(n).
공간복잡도 : ascend, descend 변수 2개만 사용하으로 O(1).
"""


class Solution:
    def validMountainArray(self, A) -> bool:
        ascend = False
        descend = False

        for i in range(1, len(A)):
            if A[i-1] < A[i]:
                if descend:
                    return False
                ascend = True
            elif A[i-1] > A[i]:
                if not ascend:
                    return False
                descend = True
            else:
                return False

        return ascend and descend
