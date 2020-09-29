# 자세한 풀이 : https://www.notion.so/leetcode-153-Find-Minimum-in-Rotated-Sorted-Array-3702cde007ee4cf092f5bdcec3b790b6


# 시간복잡도 = O(N)
# 공간복잡도 = O(1)
class LinearTimeSolution:
    def findMin(self, nums):
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return nums[i+1]

        return nums[0]


# 시간복잡도 = O(logN)
# 공간복잡도 = O(logN)
class BinarySearchSolution1:
    def findMin(self, nums):

        while True:
            if len(nums) <= 3:
                return min(nums)

            mid = len(nums) // 2

            if nums[0] > nums[mid]:
                nums = nums[:mid + 1]
                continue

            if nums[mid] > nums[-1]:
                nums = nums[mid + 1:]
                continue

            return nums[0]


# 시간복잡도 = O(logN)
# 공간복잡도 = O(1)
class BinarySearchSolution2:
    def findMin(self, nums):

        left = 0
        right = len(nums) - 1

        while True:
            mid = (left + right) // 2

            # mid를 기준으로 왼쪽에 굴절이 있는 경우 왼쪽 배열만을 대상으로 탐색하도록 right를 갱신한다.
            if nums[left] > nums[mid]:
                right = mid
                continue

            # mid를 기준으로 오른쪽에 굴절이 있는 경우 오른쪽 배열만을 대상으로 탐색하도록 left를 갱신한다.
            if nums[mid] > nums[right]:
                left = mid + 1
                continue

            # 위 조건을 만족하지 않는 것은 nums[left:right]가 rotation이 없는
            # 올바른 배열임을 뜻하므로 배열 내 최솟값인 nums[left]를 리턴한다.
            return nums[left]
