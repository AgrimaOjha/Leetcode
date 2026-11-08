# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findMode(self, root: TreeNode | None) -> list[int]:
        self.current_val = None
        self.current_count = 0
        self.max_count = 0
        self.modes = []
        
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            
            # Process current node
            if node.val == self.current_val:
                self.current_count += 1
            else:
                self.current_val = node.val
                self.current_count = 1
                
            if self.current_count > self.max_count:
                self.max_count = self.current_count
                self.modes = [node.val]
            elif self.current_count == self.max_count:
                self.modes.append(node.val)
                
            inorder(node.right)
            
        inorder(root)
        return self.modes