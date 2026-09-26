class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
        jumps = 0
        current_end = 0
        farthest = 0
        
        # We don't need to process the last element (n - 1)
        # because once we reach or exceed it, we are done.
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            
            # If we've reached the end of our current jump range,
            # we must make another jump.
            if i == current_end:
                jumps += 1
                current_end = farthest
                
                # Early exit if we can already reach or pass the last index
                if current_end >= n - 1:
                    break
                    
        return jumps