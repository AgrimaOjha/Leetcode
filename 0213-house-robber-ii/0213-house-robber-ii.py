class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def rob_linear(houses: list[int]) -> int:
            prev2 = 0
            prev1 = 0
            for money in houses:
                current = max(prev1, prev2 + money)
                prev2 = prev1
                prev1 = current
            return prev1

        # Because houses are in a circle, house[0] and house[n-1] cannot be robbed together.
        # We take the maximum of:
        # 1. Excluding the last house (nums[:-1])
        # 2. Excluding the first house (nums[1:])
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))