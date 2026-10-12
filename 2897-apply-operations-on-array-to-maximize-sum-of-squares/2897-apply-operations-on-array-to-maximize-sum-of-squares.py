class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        bit_counts = [0] * 30
        
        # Count the frequency of each bit across all numbers
        for x in nums:
            for i in range(30):
                if (x >> i) & 1:
                    bit_counts[i] += 1
                    
        # Build the k numbers by greedily assigning bits from highest to lowest place values
        max_nums = [0] * k
        for i in range(k):
            current_num = 0
            for bit in range(29, -1, -1):
                if bit_counts[bit] > 0:
                    current_num |= (1 << bit)
                    bit_counts[bit] -= 1
            max_nums[i] = current_num
            
        # Calculate the sum of squares modulo 10^9 + 7
        total_sum = sum(x * x for x in max_nums) % MOD
        return total_sum