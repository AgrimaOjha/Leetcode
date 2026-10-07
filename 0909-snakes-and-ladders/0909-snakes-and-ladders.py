from collections import deque

class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)
        
        def get_coordinates(square: int) -> tuple[int, int]:
            # Convert 1-based square index to (row, col)
            row_from_bottom = (square - 1) // n
            r = n - 1 - row_from_bottom
            
            c_offset = (square - 1) % n
            if row_from_bottom % 2 == 0:
                c = c_offset
            else:
                c = n - 1 - c_offset
                
            return r, c

        queue = deque([(1, 0)])  # (square, moves)
        visited = {1}
        
        while queue:
            curr, moves = queue.popleft()
            
            if curr == n * n:
                return moves
            
            for dice in range(1, 7):
                nxt = curr + dice
                if nxt > n * n:
                    break
                
                r, c = get_coordinates(nxt)
                
                # If there's a snake or ladder, take it
                destination = board[r][c] if board[r][c] != -1 else nxt
                
                if destination not in visited:
                    visited.add(destination)
                    queue.append((destination, moves + 1))
                    
        return -1