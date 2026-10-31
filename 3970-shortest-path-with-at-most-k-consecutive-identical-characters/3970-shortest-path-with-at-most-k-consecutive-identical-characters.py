import heapq
from typing import List
from collections import defaultdict

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        # Build adjacency list: u -> list of (v, weight)
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            
        # Priority queue stores tuples of (current_weight, current_node, consecutive_count)
        # Initialize with node 0, starting weight 0, and count 1
        pq = [(0, 0, 1)]
        
        # Distance dictionary to store the minimum weight to reach state (node, count)
        dist = {}
        
        while pq:
            w, u, count = heapq.heappop(pq)
            
            # If we reached the destination node, return the accumulated weight
            if u == n - 1:
                return w
                
            # Skip if we already found a shorter path to this state
            if (u, count) in dist and dist[(u, count)] < w:
                continue
                
            # Explore neighbors
            for v, weight in adj[u]:
                # Determine the new consecutive character count
                if labels[u] == labels[v]:
                    new_count = count + 1
                else:
                    new_count = 1
                    
                # Skip if it exceeds the maximum allowed consecutive characters
                if new_count > k:
                    continue
                    
                next_weight = w + weight
                
                # If a shorter or equal path to state (v, new_count) is not found, update and push
                if (v, new_count) not in dist or next_weight < dist[(v, new_count)]:
                    dist[(v, new_count)] = next_weight
                    heapq.heappush(pq, (next_weight, v, new_count))
                    
        return -1