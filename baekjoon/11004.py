from sys import stdin


def find_kth(arr, k):
    while True:
        mid = len(arr) // 2
        if mid < k:
            k -= mid
            arr = arr[mid:]
        elif mid > k:
            arr = arr[:mid]
        else:
            return arr[k-1]


N, k = list(map(lambda x: int(x), stdin.readline().split()))
nums = list(map(lambda x: int(x), stdin.readline().split()))

nums = sorted(nums)
answer = find_kth(nums, k)
print(answer)

