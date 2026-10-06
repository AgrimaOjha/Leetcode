from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        # Build adjacency list and indegree array
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1

        # Queue all courses with 0 prerequisites
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        processed_courses = 0

        while queue:
            node = queue.popleft()
            processed_courses += 1

            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # If we processed all courses, there's no cycle
        return processed_courses == numCourses