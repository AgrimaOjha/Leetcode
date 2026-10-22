# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        
        total_sum = 0
        
        # Check if the left child is a leaf node
        if root.left and not root.left.left and not root.left.right:
            total_sum += root.left.val
            
        # Recursively traverse left and right subtrees
        total_sum += self.sumOfLeftLeaves(root.left)
        total_sum += self.sumOfLeftLeaves(root.right)
        
        return total_sum