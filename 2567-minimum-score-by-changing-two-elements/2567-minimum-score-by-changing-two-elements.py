class Solution:
    def minimizeSum(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 3:
            return 0

        nums.sort()
        return min(
            nums[-1] - nums[2],
            nums[-3] - nums[0],
            nums[-2] - nums[1],
        )