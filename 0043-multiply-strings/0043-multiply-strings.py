class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        pos = [0] * (m + n)
        
        # Multiply each digit from right to left
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                p1, p2 = i + j, i + j + 1
                
                # Add to the existing sum at position p2
                total = mul + pos[p2]
                
                pos[p2] = total % 10
                pos[p1] += total // 10
                
        # Skip leading zeros
        res = "".join(map(str, pos))
        return res.lstrip("0")