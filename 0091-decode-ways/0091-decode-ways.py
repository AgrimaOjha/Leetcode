class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0

        # prev2 = ways to decode s[:i-2], prev1 = ways to decode s[:i-1]
        prev2, prev1 = 1, 1

        for i in range(2, len(s) + 1):
            curr = 0

            # Single-digit decode: s[i-1] must be in '1'..'9'
            if s[i - 1] != "0":
                curr += prev1

            # Two-digit decode: s[i-2:i] must be an integer in 10..26
            two_digit = int(s[i - 2 : i])
            if 10 <= two_digit <= 26:
                curr += prev2

            prev2, prev1 = prev1, curr

        return prev1