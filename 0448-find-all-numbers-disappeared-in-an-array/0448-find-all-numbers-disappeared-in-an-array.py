class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        # Mark the presence of each number by negating the value at its corresponding index
        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
                
        # Collect all indices that remain positive, which correspond to missing numbers
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)
            else:
                # Restore the array (optional, but good practice)
                nums[i] = -nums[i]
                
        return result