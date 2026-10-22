class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        result = []
        for h in range(12):
            for m in range(60):
                # Count the total number of set bits (1s) in both hour and minute
                if (bin(h) + bin(m)).count('1') == turnedOn:
                    # Format minute with a leading zero if it's less than 10
                    result.append(f"{h}:{m:02d}")
        return result