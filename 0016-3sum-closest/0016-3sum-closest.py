class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = float('inf')
        
        for i in range(n - 2):
            left, right = i + 1, n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # If exact match found, return immediately
                if current_sum == target:
                    return current_sum
                
                # Update closest_sum if current triplet is closer to target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Adjust pointers based on comparison
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
                    
        return closest_sum