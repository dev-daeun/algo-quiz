from collections import Counter


class SolutionByHashTable:
    '''
    Counter는 dict를 상속받은 클래스이므로 해시테이블에 속한다.
    nums를 순회하면서 갯수를 세므로 Counter를 생성하는 데 걸리는 시간복잡도는 O(n).
    Counter객체 내 entry를 순회하면서 유니크한 숫자를 찾는 데 걸리는 시간복잡도는 O(n).
    따라서 총 시간복잡도 = O(n)
    해시테이블 자료구조를 추가로 사용했으므로 공간복잡도 = O(n)
    '''
    def singleNumber(self, nums):
        c = Counter(nums)
        for key, value in c.items():
            if value == 1:
                return key


class SolutionByMath:
    '''
    2 * (a + b + c) - (a + a + b + b + c) = c
    시간복잡도 = O(n)
    set을 사용했으므로 공간복잡도 = O(n)
    '''
    def singleNumber(self, nums):
        return 2 * sum(set(nums)) - sum(nums)


class SolutionByBitManipulation:
    '''
    XOR 연산 : 두 값이 다를 때 참, 같을 때 거짓

    0 XOR 0 = 0
    0 XOR 1 = 1
    1 XOR 0 = 1
    1 XOR 1 = 0

    a XOR b XOR a = a XOR a XOR b = 0 XOR b = b
    '''
    def singleNumber(self, nums):
        result = 0
        for n in nums:
            result = result ^ n
        return result
