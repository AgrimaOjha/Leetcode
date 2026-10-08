class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # Store the complete word at the leaf/end node

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        # 1. Build the Trie
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word

        ROWS, COLS = len(board), len(board[0])
        result = []

        # 2. Backtracking DFS with Trie Pruning
        def dfs(r, c, parent_node):
            char = board[r][c]
            curr_node = parent_node.children[char]

            # Check if we matched a full word
            if curr_node.word:
                result.append(curr_node.word)
                curr_node.word = None  # Prevent duplicate additions

            # Mark cell as visited
            board[r][c] = '#'

            # Explore 4-directional neighbors
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = r + dr, c + dc
                if (0 <= nr < ROWS and 0 <= nc < COLS and 
                    board[nr][nc] in curr_node.children):
                    dfs(nr, nc, curr_node)

            # Restore original character (backtrack)
            board[r][c] = char

            # Optimization: Remove leaf nodes to prune searched branches early
            if not curr_node.children:
                parent_node.children.pop(char)

        # 3. Trigger DFS from every board cell that matches a root Trie prefix
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in root.children:
                    dfs(r, c, root)

        return result