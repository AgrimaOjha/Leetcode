class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        n = len(s)
        if n < 4 or n > 12:
            return []

        res: list[str] = []
        current: list[str] = []

        def backtrack(start: int) -> None:
            # Found 4 segments
            if len(current) == 4:
                if start == n:
                    res.append(".".join(current))
                return

            # Pruning: remaining segments needed vs remaining characters
            segments_left = 4 - len(current)
            chars_left = n - start
            if chars_left < segments_left or chars_left > segments_left * 3:
                return

            # Try segment lengths of 1, 2, or 3
            for length in range(1, 4):
                if start + length > n:
                    break

                part = s[start : start + length]

                # Reject leading zeros for multi-digit segments
                if length > 1 and part[0] == "0":
                    break

                # Reject values > 255 (longer lengths from `start` will also be > 255)
                if int(part) > 255:
                    break

                current.append(part)
                backtrack(start + length)
                current.pop()

        backtrack(0)
        return res