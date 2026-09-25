class Solution:

    def setZeroes(self, matrix: list[list[int]]) -> None:
        """Do not return anything, modify matrix in-place instead.

        """
        ROWS, COLS = len(matrix), len(matrix[0])
        first_col_has_zero = False

        # Step 1: Use first row and first column as markers
        for r in range(ROWS):
            if matrix[r][0] == 0:
                first_col_has_zero = True
            for c in range(1, COLS):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        # Step 2: Zero out cells based on markers in first row & column
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # Step 3: Zero out the first row if needed
        if matrix[0][0] == 0:
            for c in range(COLS):
                matrix[0][c] = 0

        # Step 4: Zero out the first column if needed
        if first_col_has_zero:
            for r in range(ROWS):
                matrix[r][0] = 0