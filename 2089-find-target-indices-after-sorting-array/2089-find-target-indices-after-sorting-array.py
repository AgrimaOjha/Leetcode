class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        less_count = 0
        target_count = 0
        
        for num in nums:
            if num < target:
                less_count += 1
            elif num == target:
                target_count += 1
                
        return [less_count + i for i in range(target_count)]