class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        # If the required sum is greater than the max possible sum with 'num' 9s, 
        # or if sum is negative, it's impossible.
        if sum < 0 or sum > num * 9:
            return ""
        
        result = []
        for i in range(num):
            # Take as much as possible for the current digit, leaving enough 
            # for the remaining positions (at most 9 per position).
            curr = min(9, sum)
            result.append(str(curr))
            sum -= curr
            
        return "".join(result)