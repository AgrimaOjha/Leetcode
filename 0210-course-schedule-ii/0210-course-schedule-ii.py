from collections import deque, defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adj = defaultdict(list)
        in_degree = [0] * numCourses
        
        # Build adjacency list and compute in-degrees
        # [a, b] means b -> a (must take b before a)
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            in_degree[course] += 1
            
        # Queue all courses with no prerequisites (in-degree 0)
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        order = []
        
        # Topological Sort via BFS (Kahn's Algorithm)
        while queue:
            node = queue.popleft()
            order.append(node)
            
            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        # If all courses are processed, return order; otherwise a cycle exists
        return order if len(order) == numCourses else []