class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7
        
        # Helper to find where the robot lands starting a move from (r, c) in direction `d` (0: right, 1: down)
        def get_next(r, c, d):
            # d = 0 means moving right into (r, c+1)
            # d = 1 means moving down into (r+1, c)
            curr_r, curr_r_delta = r, 0
            curr_c, curr_c_delta = c, 0
            
            if d == 0:
                curr_c += 1
            else:
                curr_r += 1
                
            while 0 <= curr_r < m and 0 <= curr_c < n and grid[curr_r][curr_c] == 1:
                # Hit a mirror, reflect:
                # If entered moving right (d == 0), turn down
                # If entered moving down (d == 1), turn right
                if d == 0:
                    d = 1
                    curr_r += 1
                else:
                    d = 0
                    curr_c += 1
                    
            if not (0 <= curr_r < m and 0 <= curr_c < n):
                return None # Out of bounds
            return (curr_r, curr_c)

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        
        for i in range(m):
            for j in range(n):
                if dp[i][j] == 0:
                    continue
                
                # Try moving right (d = 0) and down (d = 1)
                for d in range(2):
                    nxt = get_next(i, j, d)
                    if nxt:
                        nr, nc = nxt
                        dp[nr][nc] = (dp[nr][nc] + dp[i][j]) % MOD
                        
        return dp[m - 1][n - 1]