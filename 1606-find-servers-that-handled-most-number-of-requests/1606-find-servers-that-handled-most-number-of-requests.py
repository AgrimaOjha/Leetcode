import heapq
import bisect

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        # Min-heap to store (free_time, server_id) for busy servers
        busy = []
        
        # Keep track of available servers using a sorted list for efficient lookup
        available = list(range(k))
        
        request_count = [0] * k
        
        for i, (arr_time, l) in enumerate(zip(arrival, load)):
            # Free up servers whose tasks are completed by the current arrival time
            while busy and busy[0][0] <= arr_time:
                _, freed_server = heapq.heappop(busy)
                
                # Insert the freed server back into the available list maintaining order
                idx = bisect.bisect_left(available, freed_server)
                available.insert(idx, freed_server)
            
            if not available:
                # All servers are busy, drop the request
                continue
            
            # Find the first available server >= (i % k)
            target = i % k
            idx = bisect.bisect_left(available, target)
            
            # If no server >= target is available, wrap around to the beginning (index 0)
            if idx == len(available):
                idx = 0
            
            server_id = available.pop(idx)
            
            # Assign the request to this server
            request_count[server_id] += 1
            heapq.heappush(busy, (arr_time + l, server_id))
            
        max_requests = max(request_count)
        return [i for i, count in enumerate(request_count) if count == max_requests]