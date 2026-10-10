class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2
        n = len(nums1)
        
        # Calculate absolute differences
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        max_diff = max(diffs)
        
        if max_diff == 0 or k == 0:
            return sum(d * d for d in diffs)
        
        # Frequency bucket array
        count = [0] * (max_diff + 1)
        for d in diffs:
            count[d] += 1
            
        # Reduce differences greedily from max_diff down to 1
        for d in range(max_diff, 0, -1):
            if count[d] == 0:
                continue
            
            # Number of reductions we can apply at level d
            take = min(k, count[d])
            count[d] -= take
            count[d - 1] += take
            k -= take
            
            if k == 0:
                break
                
        # Calculate minimum sum of squared difference
        return sum(count[d] * (d * d) for d in range(1, max_diff + 1))