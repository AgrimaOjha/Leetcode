class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # Remove dashes and convert to uppercase
        clean_s = s.replace("-", "").upper()
        
        res = []
        count = 0
        
        # Traverse from right to left
        for char in reversed(clean_s):
            if count == k:
                res.append('-')
                count = 0
            res.append(char)
            count += 1
            
        # Reverse back to get the correct order
        return "".join(reversed(res))