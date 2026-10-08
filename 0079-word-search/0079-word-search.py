from collections import Counter

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        
        # Pruning 1: Length check
        if len(word) > ROWS * COLS:
            return False
            
        # Pruning 2: Character count check
        board_counts = Counter(char for row in board for char in row)
        word_counts = Counter(word)
        for char, count in word_counts.items():
            if board_counts[char] < count:
                return False
                
        # Pruning 3: Reverse word if start character is more frequent than end character
        if board_counts[word[0]] > board_counts[word[-1]]:
            word = word[::-1]

        def dfs(r: int, c: int, idx: int) -> bool:
            if idx == len(word):
                return True
            
            if (r < 0 or r >= ROWS or 
                c < 0 or c >= COLS or 
                board[r][c] != word[idx]):
                return False
            
            # Temporarily mark as visited
            temp = board[r][c]
            board[r][c] = '#'
            
            # Explore 4 directions
            found = (dfs(r + 1, c, idx + 1) or
                     dfs(r - 1, c, idx + 1) or
                     dfs(r, c + 1, idx + 1) or
                     dfs(r, c - 1, idx + 1))
                     
            # Backtrack
            board[r][c] = temp
            return found

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True

        return False