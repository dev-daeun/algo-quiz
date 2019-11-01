def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def build_heap(nums):
    N = len(nums)
    for i in range(N // 2, -1, -1):
        nums = sift_down(nums, i)
    return nums


def sift_down(nums, i):
    N = len(nums)
    smaller = i

    while True:
        if left(i) < N and nums[left(i)] < nums[i]:
            smaller = left(i)
        if right(i) < N and nums[right(i)] < nums[smaller]:
            smaller = right(i)
        if smaller != i:
            nums[i], nums[smaller] = nums[smaller], nums[i]
        else:
            return nums
        i = smaller


def pop_from_heap(nums):
    root = nums[0]
    nums[0], nums[-1] = nums[-1], nums[0]
    nums.pop()
    sift_down(nums, 0)
    return root


class Solution:

    def sortArray(self, nums):
        tree = build_heap(nums)
        answer = []
        for _ in range(len(nums)):
            answer.append(pop_from_heap(tree))
        return answer
