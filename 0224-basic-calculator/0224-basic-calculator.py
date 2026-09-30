class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operand = 0
        result = 0
        sign = 1  # 1 means '+', -1 means '-'

        for char in s:
            if char.isdigit():
                # Form multi-digit numbers
                operand = (operand * 10) + int(char)
            elif char == '+':
                # Evaluate the expression to the left
                result += sign * operand
                sign = 1
                operand = 0
            elif char == '-':
                # Evaluate the expression to the left
                result += sign * operand
                sign = -1
                operand = 0
            elif char == '(':
                # Push the result and sign onto the stack for later
                stack.append(result)
                stack.append(sign)
                # Reset for the sub-expression inside parentheses
                sign = 1
                result = 0
            elif char == ')':
                # Evaluate the remaining sub-expression inside parentheses
                result += sign * operand
                # Pop sign and previous result
                result *= stack.pop()  # stack.pop() is the sign before '('
                result += stack.pop()  # stack.pop() is the result before '('
                operand = 0

        return result + (sign * operand)