from typing import List

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        # Sort logs by timestamp
        logs.sort(key=lambda item: item[1])
        
        # Pair queries with their original indices and sort by query time
        indexed_queries = sorted(enumerate(queries), key=lambda item: item[1])
        
        ans = [0] * len(queries)
        server_count = {}
        active_servers = 0
        
        l = 0
        r = 0
        m = len(logs)
        
        for q_idx, q_time in indexed_queries:
            window_start = q_time - x
            window_end = q_time
            
            # Expand the window to include logs <= window_end
            while r < m and logs[r][1] <= window_end:
                server_id = logs[r][0]
                if server_count.get(server_id, 0) == 0:
                    active_servers += 1
                server_count[server_id] = server_count.get(server_id, 0) + 1
                r += 1
                
            # Shrink the window to exclude logs < window_start
            while l < m and logs[l][1] < window_start:
                server_id = logs[l][0]
                server_count[server_id] -= 1
                if server_count[server_id] == 0:
                    active_servers -= 1
                l += 1
                
            # Servers with zero requests = total servers (n) - active servers in the window
            ans[q_idx] = n - active_servers
            
        return ans