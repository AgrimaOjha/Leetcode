import math

class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        
        def helper(arr):
            if len(arr) <= 2:
                return 1
            
            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]
            
            # Number of ways to interleave left and right elements, 
            # multiplied by the combinations for left and right subtrees.
            ways_left = helper(left)
            ways_right = helper(right)
            
            # math.comb computes the binomial coefficient efficiently
            comb = math.comb(len(left) + len(right), len(left))
            
            return (comb * ways_left * ways_right) % MOD

        # Subtract 1 because the problem asks for *reorderings* (excluding the original array itself)
        return (helper(nums) - 1 + MOD) % MOD