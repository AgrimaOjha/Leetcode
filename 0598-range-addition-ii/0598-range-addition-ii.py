from typing import List


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        min_rows = m
        min_cols = n

        for rows, cols in ops:
            if rows < min_rows:
                min_rows = rows
            if cols < min_cols:
                min_cols = cols

        return min_rows * min_cols