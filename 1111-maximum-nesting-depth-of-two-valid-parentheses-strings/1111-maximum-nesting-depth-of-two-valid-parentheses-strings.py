class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        ans = []
        depth = 0
        
        for char in seq:
            if char == '(':
                depth += 1
                # Assign based on the current depth parity
                ans.append(depth % 2)
            else:
                # Assign based on the current depth parity before exiting the level
                ans.append(depth % 2)
                depth -= 1
                
        return ans