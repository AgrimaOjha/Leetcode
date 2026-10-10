class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ones = 0
        twos = 0
        
        for num in nums:
            # Update ones: add current num, but remove bits already present in twos
            ones = (ones ^ num) & ~twos
            # Update twos: add bits just removed/present from ones, but remove bits present in twos
            twos = (twos ^ num) & ~ones
            
        return ones