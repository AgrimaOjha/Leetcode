class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # Sort the array to ensure we pair numbers that are as close as possible
        nums.sort()
        
        # Sum up every alternate element starting from index 0
        return sum(nums[::2])