from collections import defaultdict
from typing import List

class Solution:
    def calcEquation(
        self, 
        equations: List[List[str]], 
        values: List[float], 
        queries: List[List[str]]
    ) -> List[float]:
        # Build the graph
        graph = defaultdict(dict)
        for (u, v), val in zip(equations, values):
            graph[u][v] = val
            graph[v][u] = 1.0 / val

        def dfs(src: str, target: str, visited: set) -> float:
            # If source or target is not in graph, path doesn't exist
            if src not in graph or target not in graph:
                return -1.0
            
            # Found path
            if src == target:
                return 1.0
            
            visited.add(src)
            for neighbor, weight in graph[src].items():
                if neighbor not in visited:
                    res = dfs(neighbor, target, visited)
                    if res != -1.0:
                        return weight * res
            return -1.0

        results = []
        for src, target in queries:
            results.append(dfs(src, target, set()))
        
        return results