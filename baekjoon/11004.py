from sys import stdin


N, k = list(map(lambda x: int(x), stdin.readline().split()))
nums = list(map(lambda x: int(x), stdin.readline().split()))

nums = sorted(nums)

# 배열의 정렬이 필요할 때는 그냥 python의 built-in 함수를 쓰자.
print(nums[k-1])

