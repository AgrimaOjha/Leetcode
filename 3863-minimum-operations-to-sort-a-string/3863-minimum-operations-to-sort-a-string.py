class Solution:
    def minOperations(self, s: str) -> int:
        # 1. If already sorted, 0 operations needed
        if all(x <= y for x, y in zip(s, s[1:])):
            return 0
        
        # 2. If length is 2, single-letter substrings can't change order
        if len(s) == 2:
            return -1
            
        mid = s[1:-1]
        lo, hi = min(mid), max(mid)
        
        # 3. If first char is the smallest overall, or last char is the largest overall
        if s[0] <= min(lo, s[-1]) or max(s[0], hi) <= s[-1]:
            return 1
            
        # 4. If first char is uniquely the largest and last char is uniquely the smallest
        if s[-1] < lo <= hi < s[0]:
            return 3
            
        # 5. Otherwise, 2 operations are sufficient
        return 2