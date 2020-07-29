class Solution:
    def maxSubArray(self, nums):

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1], nums[0] + nums[1])

        start = end = 0
        i = 1
        m = nums[0]

        while i < len(nums):
            m = max(nums[i], sum(nums[start:i+1]), m)
            if nums[i] == m:
                end = i
            elif sum(nums[start:i+1]) == m:
                end = i
            i += 1

        j = start
        while j <= end:
            m = max(sum(nums[j:end+1]), m)
            if sum(nums[j:end+1]) == m:
                start = j
            j += 1

        return sum(nums[start:end+1])


s = Solution()

