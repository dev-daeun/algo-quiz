"""
small: 합이 target인 두 숫자 중에 크기가 작은 숫자의 인덱스
big: 합이 target인 두 숫자 중에 크기가 큰 숫자의 인덱스

처음에는 아래와 같이 시작한다.

* small = 배열 내 최솟값
* big = 배열 내 최댓값

small + big < target -> small이 더 커야 함. -> small += 1
small + big > target -> big이 더 작아야 함. -> big += 1
"""


class Solution:
    def twoSum(self, numbers, target):
        small = 0
        big = len(numbers) - 1

        while small != big:
            result = numbers[small] + numbers[big]
            if result < target:
                small += 1
            elif result > target:
                big -= 1
            else:
                return [small + 1, big + 1]
