# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        def helper(in_left, in_right):
            if in_left > in_right:
                return None
            
            # The last element in postorder is the current root value
            root_val = postorder.pop()
            root = TreeNode(root_val)
            
            # Root's index splits the inorder array into left and right subtrees
            index = inorder_map[root_val]
            
            # Build right subtree first because postorder processes (Left, Right, Root)
            # So popping from postorder gives roots in Reverse Postorder order (Root, Right, Left)
            root.right = helper(index + 1, in_right)
            root.left = helper(in_left, index - 1)
            
            return root

        return helper(0, len(inorder) - 1)