class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # Square all elements and sort them in ascending order
        squared = sorted(x * x for x in nums)
        n = len(squared)
        
        # The first half (smaller elements) are subtracted, the second half (larger elements) are added
        mid = n // 2
        
        # Sum of the larger half minus sum of the smaller half
        return sum(squared[mid:]) - sum(squared[:mid])