"""
딱 1번 값을 바꾼 후에도 배열은 항상 non-decreasing을 유지해야 한다.

배열 안에 연속하는 숫자 3개 n[i-1], n[i], n[i+1] 이 있고 n[i] > n[i+1] 일 때 아래와 같이 2가지 형태일 수 있다.


1.
    n[i]                n[i] = n[i+1]
    /  \                 /
n[i-1]  \       ->    n[i-1]
       n[i+1]

n[i-1] > n[i+1] 인 경우, non-decreasing을 유지하기 위해 n[i+1]의 값을 n[i]의 값으로 갱신한다.


2.
    n[i]                n[i] = n[i+1]
    /\                 /
   /  n[i+1]    ->    /
n[i-1]              n[i-1]

n[i-1] < n[i+1] 인 경우, non-decreasing을 유지하기 위해 n[i]의 값을 n[i+1]의 값으로 갱신한다.


다만, i = 0 이고 n[i] > n[i+1] 인 경우에는 non-decreasing을 유지하기 위해 무조건 n[i]의 값을 n[i+1]의 값으로 갱신한다.

위와 같이 값을 바꾸는 연산이 2번 이상 발생하면 False를, 1번 이하로 발생하면 True를 리턴한다.


시간복잡도 = O(n)
공간복잡도 = O(1)

두 숫자를 비교할 때 이전 loop에서의 오름/내림차순 형태에 따라 n[i] = n[i+1]인지 n[i+1] = n[i] 인지 결정한다는 건 대충 알았는데 결정하는 기준이 잘못됐었다.
다른 사람들의 submission 슬쩍 보고 간단하게 풀었음..
"""


class Solution:
    def checkPossibility(self, nums):
        fixed = 0

        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                if fixed >= 1:
                    return False

                if i == 0:
                    nums[i] = nums[i+1]
                else:
                    if nums[i-1] > nums[i+1]:
                        nums[i+1] = nums[i]
                    else:
                        nums[i] = nums[i+1]

                fixed += 1

        return True
