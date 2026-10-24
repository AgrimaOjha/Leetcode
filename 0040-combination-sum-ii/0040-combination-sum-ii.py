class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        candidates.sort()

        def backtrack(start: int, target: int, path: list[int]):
            if target == 0:
                res.append(list(path))
                return
            
            for i in range(start, len(candidates)):
                # Skip duplicates at the same tree level to avoid duplicate combinations
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # If the current number exceeds the remaining target, stop searching this branch
                if candidates[i] > target:
                    break
                
                path.append(candidates[i])
                backtrack(i + 1, target - candidates[i], path)
                path.pop()

        backtrack(0, target, [])
        return res