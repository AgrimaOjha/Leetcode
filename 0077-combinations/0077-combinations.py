class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []
        
        def backtrack(start: int, path: list[int]):
            if len(path) == k:
                res.append(path.copy())
                return
            
            # Pruning: stop early if remaining elements aren't enough to reach size k
            for i in range(start, n - (k - len(path)) + 2):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()

        backtrack(1, [])
        return res