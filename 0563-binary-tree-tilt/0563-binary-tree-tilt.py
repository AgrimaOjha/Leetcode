# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.total_tilt = 0
        
        def dfs(node):
            if not node:
                return 0
            
            # Recursively get the sum of left and right subtrees
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            
            # Add the tilt of the current node to the total sum
            self.total_tilt += abs(left_sum - right_sum)
            
            # Return the total sum of the subtree rooted at this node
            return node.val + left_sum + right_sum
        
        dfs(root)
        return self.total_tilt