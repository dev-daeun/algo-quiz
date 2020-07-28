class MySolution:
    def rotate(self, nums, k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        save_idx = save_val = None

        for i in range(len(nums)):
            if save_idx is not None:
                new_idx = (save_idx + k) % len(nums)
                new_val = nums[new_idx]
                nums[new_idx] = save_val
                save_val = new_val
                save_idx = new_idx
            else:
                save_idx = (i + k) % len(nums)
                save_val = nums[save_idx]
                nums[save_idx] = nums[i]


# 풀이 : https://www.notion.so/leetcode-189-Rotate-Array-1ebec6b9d78a472ea5aab43da3150c21


class SolutionCyclicReplacement:
    def rotate(self, nums, k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        cnt = 0

        while cnt < len(nums):
            cur_idx = start
            cur_val = nums[cur_idx]
            while True:
                next_idx = (cur_idx + k) % len(nums)
                nums[next_idx], cur_val = cur_val, nums[next_idx]
                cur_idx = next_idx
                cnt += 1

                if cur_idx == start:
                    break

            start += 1


class SolutionReverseArray:
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def rotate(self, nums, k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # k가 배열의 길이보다 클 수 있다.
        k = k % len(nums)

        # 전체 배열을 역순으로 정렬 [1,2,3,4,5,6,7] -> [7,6,5,4,3,2,1]
        self.reverse(nums, 0, len(nums) - 1)

        # 0 ~ (k-1) 번째 부분배열을 다시 정순으로 정렬 [7,6,5,4,3,2,1] -> [5,6,7,4,3,2,1]
        self.reverse(nums, 0, k - 1)

        # k ~ 마지막 번째 부분배열을 다시 정순으로 졍렬 [5,6,7,4,3,2,1] -> [5,6,7,1,2,3,4]
        self.reverse(nums, k, len(nums) - 1)
