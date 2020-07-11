# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
# Hint:
# A two-pointer approach could be helpful here.
# The idea would be to have one pointer for iterating the array and another pointer that just works on the non-zero elements of the array.

'''
: 배열 내 0을 세는 용도.

배열을 순회하면서 nums[i]가 0일 경우 cnt_zero를 증가시킨다.
nums[i]가 0이 아닐 경우 nums[i - count_zero] 를 nums[i]로 바꾸고, nums[i]는 0으로 바꾼다.

예)
0 1 0 0 3 12 -> i = 1 일 때 count_zero = 1 -> i - count_zero = 1 - 1 = 0 -> 1 0 0 0 3 12
1 0 0 0 3 12 -> i = 4 일 때 count_zero = 3 -> i - count_zero = 4 - 3 = 1 -> 1 3 0 0 0 12
1 3 0 0 0 12 -> i = 5 일 때 count_zero = 3 -> i - count_zero = 5 - 3 = 2 -> 1 3 12 0 0 0

nums[0]이 0이 아닐 경우에는 값을 바꾸면 안되므로 분기가 추가로 필요하다.

시간복잡도 = O(n)
공간복잡도 = O(1)
'''


class Solution:
    def moveZeroes(self, nums) -> None:
        count_zero = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count_zero += 1
            else:
                if count_zero > 0:
                    nums[i - count_zero], nums[i] = nums[i], 0
