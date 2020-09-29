class Solution:
    def search(self, nums, target):
        if not nums:
            return -1

        left = 0
        right = len(nums) - 1

        # 1. 배열 안에서 최솟값(굴절의 시작)을 찾는다.
        while True:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
                continue
            if nums[left] > nums[mid]:
                right = mid
                continue
            min_idx = left
            break

        # 2. 최솟값을 기준으로 각각 왼쪽/오른쪽 부분배열은 오름차순으로 올바르게 정렬되어 있으므로 왼쪽/오른쪽 배열 중 어느 곳을 이진탐색할지 정한다.
        if min_idx != 0:
            if target <= nums[-1]:
                left = min_idx
                right = len(nums) - 1
            if target >= nums[0]:
                left = 0
                right = min_idx - 1

        # 3. 선택한 부분배열을 이진탐색한다.
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                right = mid - 1
            if nums[mid] < target:
                left = mid + 1

        return -1
