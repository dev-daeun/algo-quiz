class Solution:
    def findDisappearedNumbers(self, nums):
        # (배열에 1번 이상 출현한 숫자 - 1)를 인덱스로 갖는 숫자는 음수로 갱신된다.
        # (음수로 갱신되지 않은 숫자의 인덱스 + 1)이 배열에 나타나지 않은 숫자다.
        for n in nums:
            idx = abs(n) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]
