class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        # Start with the bottom row as our base DP array
        dp = list(triangle[-1])
        
        # Iterate from the second-to-last row up to the top
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
                
        return dp[0]