from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        parts = [str(num) for num in nums]

        def compare(a: str, b: str) -> int:
            if a + b > b + a:
                return -1  # a comes before b
            if a + b < b + a:
                return 1   # b comes before a
            return 0

        parts.sort(key=cmp_to_key(compare))

        if parts[0] == "0":
            return "0"

        return "".join(parts)