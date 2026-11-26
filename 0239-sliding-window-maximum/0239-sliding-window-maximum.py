from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq: deque[int] = deque()  # stores indices, nums[dq] is decreasing
        res: list[int] = []

        for i, num in enumerate(nums):
            # 1. Remove indices outside the current window [i - k + 1, i]
            if dq and dq[0] <= i - k:
                dq.popleft()

            # 2. Pop smaller elements from the back since `num` dominates them
            while dq and nums[dq[-1]] <= num:
                dq.pop()

            # 3. Push current index
            dq.append(i)

            # 4. Window is valid once we have seen at least k elements
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res