class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        
        def backtrack(start_idx: int, current_path: list[int], current_sum: int):
            if current_sum == target:
                res.append(list(current_path))
                return
            if current_sum > target:
                return
            
            for i in range(start_idx, len(candidates)):
                current_path.append(candidates[i])
                # Pass `i` (not `i + 1`) because the same element can be reused
                backtrack(i, current_path, current_sum + candidates[i])
                current_path.pop()
                
        backtrack(0, [], 0)
        return res