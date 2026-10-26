class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        res = 0
        
        while left <= right:
            mid = (left + right) // 2
            # Total coins needed for 'mid' complete rows: k * (k + 1) / 2
            coins_needed = mid * (mid + 1) // 2
            
            if coins_needed <= n:
                res = mid
                left = mid + 1  # Try to fit more rows
            else:
                right = mid - 1  # Too many coins required, reduce rows
                
        return res