import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        # Min-heap for available servers: stores (weight, index)
        available = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(available)
        
        # Min-heap for busy servers: stores (free_time, weight, index)
        unavailable = []
        
        ans = []
        t = 0  # current time
        
        for j, task_time in enumerate(tasks):
            t = max(t, j)
            
            # If no servers are available, jump time to when the next server is freed
            if not available and unavailable[0][0] > t:
                t = unavailable[0][0]
            
            # Move all servers that have finished their tasks back to 'available'
            while unavailable and unavailable[0][0] <= t:
                free_time, w, i = heapq.heappop(unavailable)
                heapq.heappush(available, (w, i))
            
            # Assign the task to the best available server
            w, i = heapq.heappop(available)
            ans.append(i)
            
            # Push the server into unavailable with its new release time
            heapq.heappush(unavailable, (t + task_time, w, i))
            
        return ans