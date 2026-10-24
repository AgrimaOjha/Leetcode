class Solution:
    def isNumber(self, s: str) -> bool:
        seen_digit = False
        seen_exponent = False
        seen_dot = False
        can_sign = True  # A sign is allowed at the start or immediately after an exponent
        
        for i, char in enumerate(s):
            if char.isdigit():
                seen_digit = True
                can_sign = False
            elif char in "+-":
                if not can_sign:
                    return False
                can_sign = False
            elif char == '.':
                if seen_exponent or seen_dot:
                    return False
                seen_dot = True
                can_sign = False
            elif char in "eE":
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                can_sign = True  # An exponent can be followed by a sign (e.g., "1e-5")
                seen_digit = False # Reset to ensure there are digits after 'e'
            else:
                return False
                
        return seen_digit