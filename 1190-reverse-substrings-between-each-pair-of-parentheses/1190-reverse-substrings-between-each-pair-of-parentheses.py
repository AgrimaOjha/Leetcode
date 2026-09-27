class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        stack = []
        pair = [0] * n
        
        # Step 1: Find matching pairs of parentheses
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                j = stack.pop()
                pair[i] = j
                pair[j] = i
                
        # Step 2: Traverse and build the string
        res = []
        i = 0
        direction = 1  # 1 for left-to-right, -1 for right-to-left
        
        while i < n:
            if s[i] == '(' or s[i] == ')':
                i = pair[i]       # Teleport to the paired bracket
                direction = -direction  # Reverse direction
            else:
                res.append(s[i])
            i += direction
            
        return "".join(res)