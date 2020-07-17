import heapq

"""
nums를 heapify 하는 데 걸리는 시간복잡도 = O(N) (디폴트로 최소 힙 트리로 만든다.)
min heap 에서 최소값을 뽑는 데 걸리는 시간복잡도 = O(logN)
min heap으로 만들어진 nums에서 k번째 큰 수 = len(nums) - k 번째로 작은 수를 뽑는 데 걸리는 시간복잡도 = O((len(N) - k) * logN)

따라서 총 시간복잡도 = O(N + (len(N) - k) * logN)

공간복잡도 = O(1) (기존의 nums를 변형해서 힙 트리를 만들기 때문에.)
"""


class Solution:
    def findKthLargest(self, nums, k):
        heapq.heapify(nums)

        for i in range(len(nums) - k):
            heapq.heappop(nums)

        return heapq.heappop(nums)

