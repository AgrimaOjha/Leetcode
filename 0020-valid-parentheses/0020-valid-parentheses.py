class Solution:
    def isValid(self, s: str) -> bool:
        # A stack to keep track of opening brackets
        stack = []
        # Mapping of closing brackets to their corresponding opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in bracket_map:
                # Pop top element if stack isn't empty, else assign a dummy value
                top_element = stack.pop() if stack else '#'
                
                # Check if the popped opening bracket matches the expected one
                if bracket_map[char] != top_element:
                    return False
            else:
                # Push opening brackets onto the stack
                stack.append(char)

        # Valid only if all opened brackets were matched and popped
        return not stack